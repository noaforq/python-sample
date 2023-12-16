from app.choices.base import BaseIntEnum


class OccupationalAbilityStatus(BaseIntEnum):
    """
    職業能力開発・向上に関する状況
    """

    TRAINING = 1, "研修の有無及び内容"
    SELF_ENLIGHTENMENT = 2, "自己啓発支援の有無及び内容"
    MENTOR = 3, "メンター制度の有無"
    CAREER_CONSULTING = 4, "キャリアコンサルティング制度の有無及び内容"
    IN_HOUSE_TEST = 5, "社内検定等の制度の有無及び内容"
