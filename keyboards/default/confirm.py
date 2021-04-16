from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from middlewares import _


def generate_confirm(row_width: int = 2, lang: str = 'ru'):
    kb = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)
    kb.insert(_('confirm'))
    kb.insert(_('back'))
    return kb
