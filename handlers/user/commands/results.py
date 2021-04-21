from pathlib import Path

from aiogram import types
from bot import BOT
from aiogram.dispatcher import FSMContext
from loguru import logger
from utils.misc.allow_group import allow_group
from data.config import ALLOWED_GROUPS, TABLES_FOLDER
import os
from utils.misc.excel import _file_prefix


@allow_group(allowed_ids=ALLOWED_GROUPS)
async def results(message: types.Message, state: FSMContext):
    path = TABLES_FOLDER if TABLES_FOLDER else str(Path(__file__).parent.parent.parent.parent / 'tables')
    for filename in (name for name in os.listdir(path) if _file_prefix in name):
        with open(os.path.join(path, filename), 'rb') as file:
            try:
                await BOT.send_document(message.chat.id, (filename, file))
            except Exception as e:
                logger.error(e)
