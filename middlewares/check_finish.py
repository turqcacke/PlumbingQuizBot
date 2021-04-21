from loguru import logger
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import CancelHandler
from states.user import GeneralStates, UserDataConsts
from middlewares import _
from data.config import ALLOWED_GROUPS


class CheckFinish(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        chat_id = str(update.message.chat.id) if update.message else None
        if chat_id and chat_id != update.message.from_user.id and chat_id not in ALLOWED_GROUPS:
            logger.info(update.message.chat.id)
            raise CancelHandler

    async def on_process_message(self, message: types.Message, data: dict):
        state: FSMContext = data.get('state')
        c_state = await state.get_state()
        context = await state.get_data()
        if c_state == GeneralStates.finished.state and message.text != '/cancel':
            await message.answer(_('finished', locale=context[UserDataConsts.LANG]))
            raise CancelHandler
        return
