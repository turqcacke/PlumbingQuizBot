from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from middlewares import _
from states.user import QuizStates, UserDataConsts, GeneralStates
from keyboards.default import generate_q1_ans, generate_q2_ans, generate_back
from utils.misc.polls import stop_poll
from bot import BOT

f_name = 'generate_q{}_ans'
generate_q4_ans = generate_back
generate_q5_ans = generate_back


async def confirm_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    last_question = data[UserDataConsts.LAST_QUESTION][-1]
    next_question = int(last_question) + 1

    try:
        next_state = QuizStates.__getattribute__(QuizStates, f'q{next_question}')
    except AttributeError:
        await GeneralStates.finished.set()
        await message.answer(_('answer written', locale=data[UserDataConsts.LANG]), reply_markup=ReplyKeyboardRemove())
        return

    if last_question == QuizStates.q2.state[-1]:
        await GeneralStates.confirm_answer.set()
        await BOT.send_poll(chat_id=message.chat.id,
                            question=_(f'q{next_question}'),
                            options=[_(f'q3a1', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a2', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a3', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a4', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a4', locale=data[UserDataConsts.LANG])],
                            allows_multiple_answers=True,
                            is_anonymous=False)
        async with state.proxy() as data:
            data[UserDataConsts.LAST_STATE] = data[UserDataConsts.LAST_QUESTION]
            data[UserDataConsts.LAST_QUESTION] = next_state.state
            data[UserDataConsts.Q3_id] = message.message_id
        return

    elif last_question == QuizStates.q3.state[-1]:
        if UserDataConsts.Q3 not in data or not data[UserDataConsts.Q3]:
            await message.answer(_('nothing chosen', locale=data[UserDataConsts.LANG]))
            return
        await stop_poll(message.chat.id, data)
        await state.update_data({UserDataConsts.LAST_STATE: data[UserDataConsts.LAST_QUESTION]})

    await state.update_data({UserDataConsts.LAST_QUESTION: next_state.state})
    await state.set_state(next_state)
    await message.answer(_(f'q{next_question}'),
                         reply_markup=globals().get(f_name.format(next_question))(lang=data[UserDataConsts.LANG]) \
                             if f_name.format(next_question) in globals() else None)
