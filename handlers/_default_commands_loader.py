from enum import Enum

from aiogram import types
from aiogram import Dispatcher


class Commands(Enum):
    start = 'start'
    help = 'help'
    reset = 'reset'
    changelang = 'changelang'

    def __str__(self):
        return '/' + self.value


async def setup_commands(dp: Dispatcher):
    """Binding bot / default commands"""
    await dp.bot.set_my_commands([
        types.BotCommand(str(Commands.start), "Запустить бота"),
        types.BotCommand(str(Commands.help), "Помощь"),
        types.BotCommand(str(Commands.reset), "Сначала"),
        types.BotCommand(str(Commands.changelang), "Сменнить язык")
    ])
