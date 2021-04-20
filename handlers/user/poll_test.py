from aiogram.types import PollAnswer, User
from loguru import logger
from bot import BOT
from bot import DP


async def poll_handler(poll: PollAnswer):
    logger.info(poll.as_json())
    state = DP.current_state(chat=poll.user.id, user=poll.user.id)
    logger.info(await state.get_data())
    BOT.stop_poll(chat_id=poll.user.id,)
