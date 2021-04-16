from aiogram import Dispatcher
from aiogram.types import ContentTypes
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.dispatcher.filters import Text
from handlers.user.commands import bot_help
from handlers.user.commands import bot_start
from handlers.user.language import language_choose, invalid_language
from handlers.user.q1 import q1_handler, invalid_type
from keyboards.default.language import _locales
from states.user import GeneralStates, QuizStates


def setup(dp: Dispatcher):
    """Setup handlers for bot Dispatcher"""
    dp.register_message_handler(bot_start, CommandStart(), state='*')

    dp.register_message_handler(language_choose,
                                Text(equals=_locales),
                                content_types=ContentTypes.TEXT,
                                state=GeneralStates.language)
    dp.register_message_handler(invalid_language,
                                state=GeneralStates.language)

    dp.register_message_handler(q1_handler,
                                content_types=Text,
                                state=QuizStates.q1)
    dp.register_message_handler(invalid_type,
                                state=QuizStates.q1)

    dp.register_message_handler(bot_help, CommandHelp())
