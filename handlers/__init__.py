from . import errors
from ._default_commands_loader import Commands, setup_commands
from .user import setup as setup_handlers
from .errors import setup as setup_errors
from aiogram import Dispatcher


async def setup(dp: Dispatcher):
    """
    Binding commands and setup handlers.
    """
    setup_errors(dp)
    setup_handlers(dp)
    await setup_commands(dp)


__all__ = [
    "user",
    "Commands",
    "setup"
]
