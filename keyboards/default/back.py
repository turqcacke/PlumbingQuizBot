from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from middlewares import _


def generate_back(row_width: int = 1, lang: str = 'ru'):
    kb = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)
    kb.insert(_('back'))
    return kb