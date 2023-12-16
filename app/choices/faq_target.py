from app.choices.base import BaseIntEnum


class FaqTarget(BaseIntEnum):
    """
    質問ターゲット
    """

    USER = 1, "ユーザ"
    COMPANY = 2, "企業"
    SCHOOL = 3, "学校"
