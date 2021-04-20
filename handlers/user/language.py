from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataConsts, QuizStates
from middlewares import _
from keyboards.default import generate_q1_ans
from utils.misc.quiz_utils import go_to_last_question


async def invalid_language(message: types.Message, state: FSMContext):
    await message.answer('ru | uz')


async def language_choose(message: types.Message, state: FSMContext):
    lang = message.text
    data = await state.get_data()

    await message.answer(_('language {lang}', locale=lang).format(lang=lang))
    await state.update_data({UserDataConsts.LANG: lang})

    if data:
        await go_to_last_question(message, state, data)
        return

    await message.answer(_('started', locale=lang))
    await state.update_data({UserDataConsts.LAST_STATE: await state.get_state()})
    await QuizStates.q1.set()
    await state.update_data({UserDataConsts.LAST_QUESTION: QuizStates.q1.state})

    await message.answer(_('q1', locale=lang), reply_markup=generate_q1_ans(lang=lang))
