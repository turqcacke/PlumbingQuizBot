from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import UserDataEnum, GeneralStates, QuizStates
from middlewares import _


async def back_handler(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    data = await state.get_data()
    if cur_state == GeneralStates.confirm_answer:
        await data[UserDataEnum.LAST_QUESTION].set()
