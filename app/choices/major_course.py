from app.choices.base import BaseIntEnum


class MajorCourse(BaseIntEnum):
    """
    専攻の種類(文理区分)
    """

    NOT_SELECTED = 0, "未選択"
    SCIENCE = 1, "理系"
    ARTS = 2, "文系"
    OTHER = 3, "その他"
