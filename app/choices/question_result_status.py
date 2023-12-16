from app.choices.base import BaseIntEnum


class QuestionResultStatus(BaseIntEnum):
    """
    問題解答状況
    """

    UNANSWERED = 1, "未回答"
    ANSWERING = 2, "解答中"
    PASS = 3, "合格"
    Fail = 4, "不合格"
