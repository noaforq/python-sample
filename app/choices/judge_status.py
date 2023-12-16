from app.choices.base import BaseIntEnum
from app.exceptions import InternalServerError


class JudgeStatus(BaseIntEnum):
    """
    ジャッジステータス
    """

    PA = 1, "PASSED"
    WA = 2, "WRONG ANSWER"
    CE = 3, "COMPILE ERROR"
    RE = 4, "RUNTIME ERROR"
    TLE = 5, "TIME LIMIT ERROR"
    MLE = 6, "MEMORY LIMIT ERROR"
    SE = 7, "SERVER ERROR"
    WJ = 8, "WAITING FOR JUDGING"
    TE = 9, "TEST CASE ERROR"

    @classmethod
    def from_name(cls, name: str) -> "JudgeStatus":
        for c in cls:
            if c.name == name:
                return c
        raise InternalServerError
