from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from middlewares import I18n

_locales = I18n.locales.keys()


def generate_lang_keyboard(row_width: int = 2):
    kb = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)
    for lang in _locales:
        kb.insert(KeyboardButton(lang))
    return kb
