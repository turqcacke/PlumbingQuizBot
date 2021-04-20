from aiogram.dispatcher.filters.state import State, StatesGroup


class GeneralStates(StatesGroup):
    language = State()
    finished = State()
    confirm_answer = State()


class QuizStates(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()

    @classmethod
    def get_all(cls):
        return [cls.q1, cls.q2, cls.q3, cls.q4, cls.q5]


class Q3(StatesGroup):
    add = State()
