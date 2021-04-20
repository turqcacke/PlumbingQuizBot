from middlewares import _
from aiogram import types
from aiogram.dispatcher import FSMContext

from states.user import UserDataConsts


async def help(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await msg.answer(_('help', locale=data[UserDataConsts.LANG]))
