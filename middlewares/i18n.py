from typing import Tuple, Any, Union
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from loguru import logger


class I18nWithSkip(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> Union[str, None]:
        user = types.User.get_current()
        if user:
            return await super(I18nWithSkip, self).get_user_locale(action, args)
        logger.info(types.Update.get_current().as_json())
        return
