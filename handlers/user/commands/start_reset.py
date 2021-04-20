from aiogram import types
from handlers import Commands
from aiogram.dispatcher import FSMContext
from states.user import GeneralStates
from middlewares import _
from keyboards.default.language import generate_lang_keyboard


async def start_reset(msg: types.Message, state: FSMContext):
    if msg.text == str(Commands.reset):
        await state.finish()
    await GeneralStates.language.set()
    await msg.answer(_('greetings', locale='ru') + '\n\n' + _('greetings', locale='uz'),
                     reply_markup=generate_lang_keyboard())
