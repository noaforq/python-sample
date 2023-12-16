from app.choices.base import BaseIntEnum


class QuestionResultStatusNoFail(BaseIntEnum):
    """問題解答状況(不合格なし)"""

    UNANSWERED = 1, "未回答"
    ANSWERING = 2, "解答中"
    PASS = 3, "合格"
