from aiogram import types
from utils.misc import rate_limit
from handlers import Commands
from aiogram.dispatcher import FSMContext
from loguru import logger
from states.user import GeneralStates


async def bot_help(msg: types.Message, state: FSMContext):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    logger.info(state)
    await msg.answer('\n'.join(text))
