from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from middlewares import I18n, _


def generate_q2_ans(row_width=1, lang='ru'):
    kb = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)
    kb.insert(KeyboardButton(_('q2a1', locale=lang)))
    kb.insert(KeyboardButton(_('q2a2', locale=lang)))
    kb.insert(KeyboardButton(_('q2a3', locale=lang)))
    kb.insert(KeyboardButton(_('back', locale=lang)))
    return kb
