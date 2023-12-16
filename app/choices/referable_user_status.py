from app.choices.base import BaseIntEnum


class ReferableUserStatus(BaseIntEnum):
    """紹介可能ユーザースカウト状況"""

    NOT_SCOUTED = 0, "未スカウト"
    WAITING = 1, "承諾待ち"
    APPROVED = 2, "承諾"
    REFUSED = 3, "不承諾"
    DENIED = 4, "スカウト拒否"
