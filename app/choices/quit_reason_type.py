from app.choices.base import BaseIntEnum


class QuitReasonType(BaseIntEnum):
    """退会理由種別"""

    UNATTRACTIVE_CONTENTS = 1, "コンテンツに魅力がない"
    DO_NOT_KNOW_HOW_TO_USE = 2, "使い方が分からない"
    DO_NOT_HAVE_GENRE_TO_STUDY = 3, "学習したいジャンルがない"
    UNATTRACTIVE_EVENTS = 4, "開催イベントに魅力がない"
    BAD_SUPPORT = 5, "サポートが悪い"
    CONCERN_SECURITY = 6, "セキュリティが不安"
