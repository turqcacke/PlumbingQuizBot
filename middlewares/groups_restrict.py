from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, current_handler


class RestrictGroups(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        allowed_ids = getattr(handler, 'allowed_ids', None)
        if allowed_ids and str(message.chat.id) not in allowed_ids:
            raise CancelHandler
        return
