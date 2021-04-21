from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataConsts, GeneralStates, QuizStates
from middlewares import _
from keyboards.default import generate_lang_keyboard
from utils.misc.polls import stop_poll
from utils.misc.quiz_utils import go_to_last_state


async def back_handler(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    data = await state.get_data()
    if cur_state == GeneralStates.confirm_answer.state:
        if data[UserDataConsts.LAST_QUESTION] == QuizStates.q3.state:
            await stop_poll(message.chat.id, data)
        await go_to_last_state(message, state, data)
    elif cur_state != QuizStates.q1.state:
        await go_to_last_state(message, state, data)
    else:
        await GeneralStates.language.set()
        await message.answer(_('greetings', locale='ru') + '\n\n' + _('greetings', locale='uz'),
                             reply_markup=generate_lang_keyboard())
