from middlewares import _
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ans_amount = 14
ans_locale_id = 'q1a{}'


def generate_q1_ans(row_width: int = 2, lang: str = 'ru'):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    for ans_num in range(1, ans_amount+1):
        kb.insert(KeyboardButton(_(ans_locale_id.format(ans_num), locale=lang)))
    kb.insert(KeyboardButton(_('back', locale=lang)))
    return kb
