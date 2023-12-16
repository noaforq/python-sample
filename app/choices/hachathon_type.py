from app.choices.base import BaseIntEnum


class HackathonType(BaseIntEnum):
    """ハッカソン種類"""

    FULL_STACK = 1, "フルスタック"
    API = 2, "API"
    FRONT_END = 3, "フロントエンド"
