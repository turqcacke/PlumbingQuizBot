from keyboards.default.language import _locales
from middlewares import _


def get_all_locales(msgid: str):
    words = list()
    for locale in _locales:
        words.append(_(msgid, locale=locale))
    return words
