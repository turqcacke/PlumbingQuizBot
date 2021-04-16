import asyncio
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import CancelHandler
from states.user import GeneralStates, UserDataEnum
from middlewares import _


class CheckFinish(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        state: FSMContext = data.get('state')
        c_state = await state.get_state()
        context = await state.get_data()
        if c_state == GeneralStates.finished.state:
            await message.answer(_('finished', locale=context[UserDataEnum.LANG]))
            raise CancelHandler
        return
