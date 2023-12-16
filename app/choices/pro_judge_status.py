from app.choices.base import BaseIntEnum
from app.exceptions import InternalServerError


class ProJudgeStatus(BaseIntEnum):
    """
    PROジャッジステータス
    """

    WAITING_FOR_JUDGING = 1, "ジャッジ実行中"
    SAMPLE_CASE_ERROR = 2, "サンプル実行失敗"
    TEST_CASE_ERROR = 3, "テスト実行失敗"
    WRONG_ANSWER = 4, "不合格"
    PASSED = 5, "合格"
    SERVER_ERROR = 6, "サーバーエラー"

    @classmethod
    def from_name(cls, name: str) -> "ProJudgeStatus":
        for c in cls:
            if c.name == name:
                return c
        raise InternalServerError
