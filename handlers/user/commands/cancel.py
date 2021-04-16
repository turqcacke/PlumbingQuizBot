from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def cancel_and_reset(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('State reseated')
