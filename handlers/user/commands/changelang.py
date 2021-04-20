from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.default import generate_lang_keyboard
from middlewares import _
from states.user import UserDataConsts
from states.user import GeneralStates


async def changelang(message: Message, state: FSMContext):
    data = await state.get_data()
    await GeneralStates.language.set()
    await message.answer(_('language', locale=data[UserDataConsts.LANG]),
                         reply_markup=generate_lang_keyboard())
