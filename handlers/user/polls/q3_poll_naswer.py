from aiogram import types
from bot import DP
from states.user import UserDataConsts, QuizStates
from middlewares import _


async def q3_poll_answer(poll: types.PollAnswer):
    state = DP.current_state(chat=poll.user.id, user=poll.user.id)
    async with state.proxy() as data:
        if data[UserDataConsts.LAST_QUESTION] == QuizStates.q3.state:
            data[UserDataConsts.Q3] = list()
            for ans in poll.option_ids:
                data[UserDataConsts.Q3].append(_(f'q3a{ans + 1}', locale=data[UserDataConsts.LANG]))
