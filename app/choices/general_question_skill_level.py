from app.choices.base import BaseIntEnum


class GeneralQuestionSkillLevel(BaseIntEnum):
    """
    スキルレベル(一般問題)
    """

    ELEMENTARY = 1, "初級"
    INTERMEDIATE = 2, "中級"
    ADVANCED = 3, "上級"

    @classmethod
    def make_choice(cls, value: int) -> "GeneralQuestionSkillLevel":
        match value:
            case value if value <= 3:
                return cls.ELEMENTARY
            case value if value <= 6:
                return cls.INTERMEDIATE
        return cls.ADVANCED
