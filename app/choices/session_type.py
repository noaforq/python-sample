from app.choices.base import BaseIntEnum


class SessionType(BaseIntEnum):
    """
    セッション種別
    """

    NORMAL = 1, "通常セッション"
    PRO = 2, "PROセッション"
    TECHTHON = 3, "Techthonセッション"
