from app.choices.base import BaseIntEnum


class SessionUserStatus(BaseIntEnum):
    """
    セッションユーザーステータス
    """

    NOT_SET = 0, "未設定"
    BEFORE_ANSWERING = 1, "解答開始前"
    ANSWERING = 2, "解答中"
    END_OF_ANSWER = 3, "解答終了"
    WAITING_FOR_REUNION = 4, "再会待ち"
