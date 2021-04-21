from aiogram import Dispatcher
from .i18n import I18nWithSkip
from .groups_restrict import RestrictGroups
from data.config import I18_DOMAIN, LOCALES_DIR

I18n = I18nWithSkip(domain=I18_DOMAIN, path=LOCALES_DIR)
_ = I18n.gettext


def setup(dp: Dispatcher):
    from .throttling import ThrottlingMiddleware
    from .check_finish import CheckFinish

    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(I18n)
    dp.middleware.setup(CheckFinish())
    dp.middleware.setup(RestrictGroups())
