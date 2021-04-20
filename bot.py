from typing import List, Tuple
import aiojobs as aiojobs
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.types import ParseMode
from aiohttp import web
from loguru import logger
from data import config

BOT = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
STORAGE = MemoryStorage() if not config.USE_MONGO else MongoStorage(**config.mongo)
DP = Dispatcher(BOT, storage=STORAGE)


class App:

    def __init__(self, bot: Bot, dp: Dispatcher):
        self.bot = bot
        self.dp = dp

    async def on_startup_webhook(self, app: web.Application):
        import middlewares
        import filters
        import handlers
        middlewares.setup(self.dp)
        filters.setup(self.dp)
        await handlers.setup(self.dp)
        logger.info('Configure Webhook URL to: {url}', url=config.WEBHOOK_URL)
        await self.dp.bot.set_webhook(config.WEBHOOK_URL)

    async def on_shutdown_webhook(self, app: web.Application):
        app_bot: Bot = app['bot']
        await app_bot.close()

    async def init_webhook(self) -> web.Application:
        from utils.misc import logging
        import web_handlers
        logging.setup()
        scheduler = await aiojobs.create_scheduler()
        app = web.Application()
        sub_apps: List[Tuple[str, web.Application]] = [
            ('/health/', web_handlers.health_app),
            ('/tg/webhooks/', web_handlers.tg_updates_app),
        ]
        for prefix, sub_app in sub_apps:
            sub_app['bot'] = self.bot
            sub_app['dp'] = self.dp
            sub_app['scheduler'] = scheduler
            app.add_subapp(prefix, sub_app)
        app.on_startup.append(self.on_startup_webhook)
        app.on_shutdown.append(self.on_shutdown_webhook)
        return app

    async def on_startup_polling(self, dp: Dispatcher):
        """
        Bot polling start function
        Used with param on_start in executor.start_polling()
        """
        import handlers
        import filters
        import middlewares
        from utils.misc import logging
        logging.setup()
        middlewares.setup(dp)
        filters.setup(dp)

        await handlers.setup(dp)

    async def on_shutdown_polling(self, dp: Dispatcher):
        await dp.storage.close()
        await dp.storage.wait_closed()

    def start(self):
        if config.USE_WEBHOOK:
            web.run_app(self.init_webhook())
        else:
            executor.start_polling(self.dp, skip_updates=True,
                                   on_startup=self.on_startup_polling, on_shutdown=self.on_shutdown_polling)


if __name__ == '__main__':
    app = App(bot=BOT, dp=DP)
    app.start()
