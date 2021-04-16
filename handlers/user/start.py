from aiogram import types
from utils.misc import rate_limit
from .. import Commands


@rate_limit(5, Commands.start)
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!')
