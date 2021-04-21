from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, current_handler


class RestrictGroups(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        allowed_ids = getattr(handler, 'allowed_ids', None)
        if message.chat.id == message.from_user.id or (allowed_ids and str(message.chat.id) in allowed_ids):
            return
        raise CancelHandler
