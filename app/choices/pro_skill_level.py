from app.choices.base import BaseIntEnum


class ProSkillLevel(BaseIntEnum):
    """
    スキルレベル(Pro問題)
    """

    ELEMENTARY = 1, "初級"
    INTERMEDIATE = 4, "中級"
    ADVANCED = 7, "上級"
