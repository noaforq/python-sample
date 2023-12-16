from app.choices.base import BaseIntEnum


class PassiveSmokingInitiative(BaseIntEnum):
    """
    集合場所における受動喫煙防止の取り組み
    """

    NOTHING = 1, "なし"
    NO_SMOKING_ON_SITE = 2, "敷地内禁煙あり"
    NO_SMOKING_INDOORS = 3, "屋内禁煙あり"
    NO_SMOKING_INDOORS_PRINCIPLE = 4, "屋内原則禁煙あり"
    INDOOR_SMOKING_ALLOWED = 5, "屋内喫煙可"
    OUTDOOR_SMOKING_ALLOWED = 6, "屋外喫煙可"
    OTHERS = 7, "その他、取り組みあり"
