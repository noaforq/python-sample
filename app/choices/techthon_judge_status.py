from app.choices.base import BaseIntEnum
from app.exceptions import InternalServerError


class TechthonJudgeStatus(BaseIntEnum):
    """テックソンジャッジステータス"""

    PASSED = 1, "PASSED"
    WRONG_ANSWER = 2, "WRONG ANSWER"
    ERROR = 3, "ERROR"
    WAITING = 4, "WAITING FOR JUDGING"

    @classmethod
    def from_name(cls, name: str) -> "TechthonJudgeStatus":
        for c in cls:
            if c.name == name:
                return c
        raise InternalServerError
