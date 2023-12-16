from app.choices.base import BaseIntEnum


class SessionStatus(BaseIntEnum):
    BEFORE_START = 1, "開催前"
    IN_SESSION = 2, "開催中"
    END = 3, "終了"
