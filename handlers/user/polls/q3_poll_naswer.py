from aiogram import types
from bot import DP
from states.user import UserDataConsts, QuizStates
from middlewares import _
from bot import BOT
from utils.misc.polls import stop_poll
from keyboards.default import generate_back


async def q3_poll_answer(poll: types.PollAnswer):
    state = DP.current_state(chat=poll.user.id, user=poll.user.id)
    async with state.proxy() as data:
        if data[UserDataConsts.LAST_QUESTION] == QuizStates.q3.state:
            data[UserDataConsts.Q3] = list()
            for ans in poll.option_ids:
                data[UserDataConsts.Q3].append(_(f'q3a{ans + 1}', locale=data[UserDataConsts.LANG]))

            await stop_poll(poll.user.id, data)
            await QuizStates.q4.set()
            next_state = getattr(QuizStates, f'q{int(data[UserDataConsts.LAST_QUESTION][-1])+1}')
            data[UserDataConsts.LAST_STATE] = data[UserDataConsts.LAST_QUESTION]
            data[UserDataConsts.LAST_QUESTION] = next_state.state
        await BOT.send_message(text=_('q4', locale=data[UserDataConsts.LANG]),
                               chat_id=poll.user.id,
                               reply_markup=generate_back(lang=data[UserDataConsts.LANG]))
