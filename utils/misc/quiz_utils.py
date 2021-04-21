from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import BOT
from middlewares import _

from states.user import UserDataConsts, QuizStates, GeneralStates
from keyboards.default import generate_q1_ans, generate_q2_ans, generate_back, generate_confirm

f_name = 'generate_q{}_ans'
generate_q4_ans = generate_back
generate_q5_ans = generate_back


async def go_to_last_question(message: Message, state: FSMContext, data: dict):
    last_question = data[UserDataConsts.LAST_QUESTION][-1]
    await state.set_state(data[UserDataConsts.LAST_QUESTION])
    await message.answer(_(f'q{last_question}'),
                         reply_markup=globals().get(f_name.format(last_question))(lang=data[UserDataConsts.LANG]) \
                             if f_name.format(last_question) in globals() else None)


async def go_to_last_state(message: Message, state: FSMContext, data: dict):
    last_question = int(data[UserDataConsts.LAST_STATE][-1])
    await state.update_data({UserDataConsts.LAST_STATE: getattr(QuizStates,
                                                                f'q{last_question - 1}').state
                            if last_question > 1 else GeneralStates.language.state})
    await state.update_data({UserDataConsts.LAST_QUESTION: data[UserDataConsts.LAST_STATE]})

    if data[UserDataConsts.LAST_STATE] == QuizStates.q3.state:
        await GeneralStates.confirm_answer.set()
        await state.update_data({UserDataConsts.Q3: None})
        await state.update_data({UserDataConsts.Q3_id: message.message_id})
        await BOT.send_poll(chat_id=message.chat.id,
                            question=_(f'q{last_question}', locale=data[UserDataConsts.LANG]),
                            options=[_(f'q3a1', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a2', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a3', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a4', locale=data[UserDataConsts.LANG]),
                                     _(f'q3a5', locale=data[UserDataConsts.LANG])],
                            allows_multiple_answers=True,
                            is_anonymous=False,
                            reply_markup=generate_confirm(lang=generate_back(lang=data[UserDataConsts.LANG])))
        return

    await state.set_state(data[UserDataConsts.LAST_STATE])
    await message.answer(_(f'q{last_question}'),
                         reply_markup=globals().get(f_name.format(last_question))(lang=data[UserDataConsts.LANG]) \
                             if f_name.format(last_question) in globals() else None)
