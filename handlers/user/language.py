from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataConsts, QuizStates
from middlewares import _
from keyboards.default import generate_q2_answers


async def invalid_language(message: types.Message, state: FSMContext):
    await message.answer('ru | uz')


async def language_choose(message: types.Message, state: FSMContext):
    lang = message.text
    data = await state.get_data()

    await message.answer(_('language {lang}', locale=lang).format(lang=lang))
    await state.update_data({UserDataConsts.LANG: lang})

    if data:
        return

    await message.answer(_('started', locale=lang))
    await QuizStates.q1.set()
    await state.update_data({UserDataConsts.LAST_STATE: QuizStates.q1.state})

    await message.answer(_('q1'), reply_markup=generate_q2_answers(lang=lang))
