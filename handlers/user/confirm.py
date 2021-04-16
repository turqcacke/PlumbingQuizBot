from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from middlewares import _
from states.user import QuizStates, UserDataConsts, GeneralStates


async def confirm_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    last_question = data[UserDataConsts.LAST_QUESTION][-1]
    if last_question == QuizStates.q5.state[-1]:
        await GeneralStates.finished.set()
    else:
        await state.set_state(QuizStates.__getattribute__(QuizStates, f'q{last_question + 1}'))
    await message.answer(_(''))
