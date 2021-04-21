from bot import BOT
from aiogram.utils.exceptions import MessageWithPollNotFound, MessageIsNotAPoll, PollCantBeStopped, \
    PollHasAlreadyBeenClosed
from states.user import UserDataConsts


async def stop_poll(chat_id: int, data: dict):
    for i in range(1, 30):
        try:
            await BOT.stop_poll(chat_id=chat_id, message_id=data[UserDataConsts.Q3_id] + i)
            break
        except PollHasAlreadyBeenClosed:
            break
        except PollCantBeStopped:
            await BOT.delete_message(chat_id=chat_id, message_id=data[UserDataConsts.Q3_id] + i)
            break
        except (MessageWithPollNotFound, MessageIsNotAPoll) as e:
            pass
