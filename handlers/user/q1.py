from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataConsts, QuizStates
from middlewares import _
from keyboards.default import generate_confirm


async def invalid_type(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(_('invalid type', locale=data[UserDataConsts.LANG]))


async def q1_handler(message: types.Message, state: FSMContext):
    q1_ans = message.text
    async with state.proxy() as data:
        data.update({UserDataConsts.Q1: message.text})
        data.update({UserDataConsts.LAST_QUESTION: QuizStates.q1.state})
    await message.answer(_('q1',
                           locale=data[UserDataConsts.LANG]) + '\n' + _('confirm answer {answer}').format(answer=q1_ans),
                         reply_markup=generate_confirm(lang=data[UserDataConsts.LANG]))
