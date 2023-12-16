from app.choices.base import BaseIntEnum


class QuestionResultType(BaseIntEnum):
    """
    問題解答種別
    """

    SESSION = 1, "セッション"
    CHALLENGE = 2, "チャレンジ"
    PRACTICE = 3, "プラクティス"
    LEANING = 4, "ラーニング"
    OLD_SESSION = 5, "旧セッション"
