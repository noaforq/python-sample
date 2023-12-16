from app.choices.base import BaseIntEnum


class TokenKind(BaseIntEnum):
    """
    トークン種類
    """

    ACCESS = 1
    REFRESH = 2
    EMAIL_VERIFY = 3
    PASSWORD_RESET = 4
    SIGNUP = 5
