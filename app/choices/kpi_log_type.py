from app.choices.base import BaseIntEnum


class KpiLogType(BaseIntEnum):
    """
    KPIログタイプ
    """

    ALL = 1, "総問題数"
    ALL_AND_TRASH = 2, "総問題数 + ゴミ箱"
    STOCK = 3, "ストック"
    UNPUBLISHED = 4, "非公開"
    CHALLENGE = 5, "チャレンジ"
    PRACTICE = 6, "プラクティス"
    TRASH = 7, "ゴミ箱"
    ALL_SYSTEM = 8, "全問題「システム」"
    TRANSLATED = 9, "英訳済み"
    LEARNING = 10, "ラーニング問題"
