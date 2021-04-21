from aiogram import Dispatcher
from aiogram.types import ContentTypes
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.dispatcher.filters import Text
from handlers.user.commands import help, start_reset, changelang
from handlers.user.language import language_choose, invalid_language
from handlers.user.question import question_handler, invalid_type, invalid_length, invalid_input
from handlers.user.confirm import confirm_handler
from handlers.user.back import back_handler
from states.user import GeneralStates, QuizStates
from middlewares import _
from handlers.user.commands.test import test
from handlers.user.polls.q3_poll_naswer import q3_poll_answer
from data.consts import MAX_LENGTH
from utils.misc.locales import get_all_locales


def get_q_ans(q_number, limit=15):
    words = list()
    for ans_num in range(1, limit):
        for ans in get_all_locales(f'q{q_number}a{ans_num}'):
            words.append(ans)
    return words


def setup(dp: Dispatcher):
    """Setup handlers for bot Dispatcher"""
    dp.register_poll_answer_handler(q3_poll_answer)
    dp.register_message_handler(start_reset, CommandStart(), state='*')
    dp.register_message_handler(test, commands=['test'], state='*')

    dp.register_message_handler(help,
                                CommandHelp(),
                                state=[GeneralStates.confirm_answer] + QuizStates.get_all())
    dp.register_message_handler(start_reset,
                                commands=['reset'],
                                state=[GeneralStates.confirm_answer, GeneralStates.language] + QuizStates.get_all())
    dp.register_message_handler(changelang,
                                commands=['changelang'],
                                state=[GeneralStates.confirm_answer] + QuizStates.get_all())

    dp.register_message_handler(language_choose,
                                Text(equals=_locales),
                                content_types=ContentTypes.TEXT,
                                state=GeneralStates.language)
    dp.register_message_handler(invalid_language,
                                state=GeneralStates.language)

    dp.register_message_handler(back_handler,
                                Text(equals=get_all_locales('back')),
                                state=[GeneralStates.confirm_answer] + QuizStates.get_all())
    dp.register_message_handler(confirm_handler,
                                Text(equals=get_all_locales('confirm')),
                                state=GeneralStates.confirm_answer)

    dp.register_message_handler(question_handler,
                                Text(equals=get_q_ans(1, 15)),
                                content_types=ContentTypes.TEXT,
                                state=QuizStates.q1)
    dp.register_message_handler(question_handler,
                                Text(equals=get_q_ans(2, 5)),
                                content_types=ContentTypes.TEXT,
                                state=QuizStates.q2)
    dp.register_message_handler(question_handler,
                                lambda msg: len(msg.text) < MAX_LENGTH,
                                content_types=ContentTypes.TEXT,
                                state=[QuizStates.q4, QuizStates.q5])

    dp.register_message_handler(invalid_length,
                                content_types=ContentTypes.TEXT,
                                state=[QuizStates.q4, QuizStates.q5])
    dp.register_message_handler(invalid_type,
                                state=[QuizStates.q5, QuizStates.q4])
    dp.register_message_handler(invalid_input,
                                state=[GeneralStates.confirm_answer,
                                       QuizStates.q1,
                                       QuizStates.q2])
