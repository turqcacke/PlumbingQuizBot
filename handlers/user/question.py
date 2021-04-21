from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataConsts, QuizStates, GeneralStates
from middlewares import _
from keyboards.default import generate_confirm
from data.consts import MAX_LENGTH


async def invalid_input(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(_('invalid input', locale=data[UserDataConsts.LANG]))


async def invalid_type(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(_('invalid type', locale=data[UserDataConsts.LANG]))


async def invalid_length(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(_('invalid length {max_length}', locale=data[UserDataConsts.LANG]).format(
        max_length=MAX_LENGTH))


async def question_handler(message: types.Message, state: FSMContext):
    ans = message.text
    cur_question = (await state.get_state())[-1]
    async with state.proxy() as data:
        data.update({getattr(UserDataConsts, f'Q{cur_question}'): message.text})
        data.update({UserDataConsts.LAST_STATE: await state.get_state()})
    await message.answer(_(f'q{cur_question}',
                           locale=data[UserDataConsts.LANG]) + '\n' + _('confirm answer {answer}',
                                                                        locale=data[UserDataConsts.LANG])
                         .format(answer=ans),
                         reply_markup=generate_confirm(lang=data[UserDataConsts.LANG]))
    await GeneralStates.confirm_answer.set()
