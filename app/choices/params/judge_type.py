from app.choices.base import BaseEnum


class JudgeType(str, BaseEnum):
    """ジャッジタイプ
    ジャッジシステムから受け取った結果がどこで使用されたものかを判別するためのもの
    """

    QUESTION = "question", "問題"
    QUESTION_SAMPLE = "question_sample", "問題サンプルケース"
    TEMPLATE = "template", "問題テンプレート"
    VERIFICATION = "verification", "問題検証"
