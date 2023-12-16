from app.choices.base import BaseIntEnum


class PortfolioUserSkillLevel(BaseIntEnum):
    """
    スキルレベル(ポートフォリオ用)
    """

    BEGINNER = 1, "入門"
    ELEMENTARY = 2, "初級"
    INTERMEDIATE = 3, "中級"
    ADVANCED = 4, "上級"
