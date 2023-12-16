from app.choices.base import BaseIntEnum


class QuestionAnswerResult(BaseIntEnum):
    """
    問題解答結果
    """

    SCORING = 1, "採点中"
    PASS = 2, "合格"
    FAILURE = 3, "不合格"
    COMPILE_ERROR = 4, "コンパイルエラー"
    SERVER_ERROR = 5, "サーバーエラー"
