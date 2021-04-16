from enum import Enum, auto


class UserDataEnum(Enum):
    LANG = auto()
    Q1 = auto()
    Q2 = auto()
    Q3 = auto()
    Q4 = auto()
    Q5 = auto()
    LAST_STATE = auto()
    LAST_QUESTION = auto()

    def __str__(self):
        return self.name
