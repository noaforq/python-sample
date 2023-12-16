from app.choices.base import BaseIntEnum


class SubmitType(BaseIntEnum):
    """
    採点方法
    """

    CSV = 1, "CSV"
    PROGRAM = 2, "プログラム"
