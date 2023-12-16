from app.choices.base import BaseEnum


class DownloadType(str, BaseEnum):
    ALL = "All", "テストケース・サンプルケースの全て"
    TEST = "Test", "テストケースのみ"
    SAMPLE = "Sample", "サンプルケースのみ"
