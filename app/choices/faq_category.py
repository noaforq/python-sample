from app.choices.base import BaseIntEnum


class FaqCategory(BaseIntEnum):
    """
    質問カテゴリ
    """

    QUESTION = 1, "問題について"
    EVENT_OR_TECHTHON = 2, "イベント、テックソンについて"
    PRO_OR_LEARNING = 3, "プロ、ラーニングについて"
    CHALLENGE_OR_PRACTICE = 4, "チャレンジ、プラクティスについて"
    TECHFUL = 5, "TechFULについて"
    OTHERS = 6, "その他"
