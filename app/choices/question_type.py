from app.choices.base import BaseIntEnum


class QuestionType(BaseIntEnum):
    """
    問題形式
    """

    CORDING = 1, "コーディング問題"
    FILLING = 2, "穴埋め問題"
    BUG = 3, "バグ取り問題"
    SELECTION = 4, "選択式問題"
    BLANK = 5, "空欄問題"
