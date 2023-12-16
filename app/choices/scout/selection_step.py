from app.choices.base import BaseIntEnum


class SelectionStep(BaseIntEnum):
    """
    選考ステップ
    """

    APPLYING = 10, "応募中"
    WAITING_FOR_SCOUT_ACCEPTANCE = 11, "スカウト承諾待ち"
    DOCUMENT_SCREENING = 20, "書類選考"
    FIRST_SELECTION = 21, "1次面接"
    SECOND_SELECTION = 22, "2次面接"
    THIRD_SELECTION = 23, "3次面接"
    FOURTH_SELECTION = 24, "4次面接"
    FIFTH_SELECTION = 25, "5次面接"
    UNOFFICIAL_OFFER = 30, "内定出し"
    ACCEPTED_UNOFFICIAL_OFFER = 31, "内定承諾"
    HIRED = 32, "入社済み"
    REFUSED_SCOUT = 40, "スカウト不承諾"
    NOT_ADOPTED = 41, "お見送り"
    DECLINE = 42, "辞退"
    FINISHED = 49, "終了"

    @classmethod
    def steps_in_selection(cls) -> list["SelectionStep"]:
        return [
            cls.DOCUMENT_SCREENING,
            cls.FIRST_SELECTION,
            cls.SECOND_SELECTION,
            cls.THIRD_SELECTION,
            cls.FOURTH_SELECTION,
            cls.FIFTH_SELECTION,
        ]

    @classmethod
    def steps_having_offered(cls) -> list["SelectionStep"]:
        return [
            cls.UNOFFICIAL_OFFER,
            cls.ACCEPTED_UNOFFICIAL_OFFER,
            cls.HIRED,
        ]
