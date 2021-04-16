from aiogram import types
from utils.misc import rate_limit
from handlers import Commands
from bot import DP
from aiogram.dispatcher import FSMContext
from loguru import logger
from states.user import GeneralStates
from middlewares import _
from keyboards.default.language import generate_lang_keyboard


async def bot_start(msg: types.Message, state: FSMContext):
    await GeneralStates.language.set()
    await msg.answer(_('greetings', locale='ru') + '\n\n' + _('greetings', locale='uz'),
                     reply_markup=generate_lang_keyboard())
