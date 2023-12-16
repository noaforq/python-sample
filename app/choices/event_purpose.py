from app.choices.base import BaseIntEnum


class EventPurpose(BaseIntEnum):
    """
    イベントの目的
    """

    PROGRAMMING_CONTEST = 1, "プログラミングコンテスト"
    TEST = 2, "試験、テスト"
    LESSON = 3, "講義、授業"
    SKILL_CHECK = 4, "スキルチェック"
    CERTIFICATE_EXAM = 5, "検定試験"
    VERIFICATION = 6, "検証用"
    TCB = 7, "TCB"
    OTHERS = 8, "その他"
