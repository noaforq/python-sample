from app.choices.base import BaseEnum


class Locale(str, BaseEnum):
    """ロケール"""

    JA = "ja", "日本語"
    EN = "en", "英語"
