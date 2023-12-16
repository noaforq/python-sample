from app.choices.base import BaseEnum


class Severity(str, BaseEnum):
    DEFAULT = "DEFAULT", "デフォルト"
    INFO = "INFO", "情報"
    DEBUG = "DEBUG", "デバッグ"
    NOTICE = "NOTICE", "お知らせ"
    WARNING = "WARNING", "警告"
    ERROR = "ERROR", "エラー"
    CRITICAL = "CRITICAL", "重大"
    ALERT = "ALERT", "アラート"
    EMERGENCY = "EMERGENCY", "緊急"
