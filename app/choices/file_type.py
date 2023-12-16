from app.choices.base import BaseIntEnum


class FileType(BaseIntEnum):
    """ファイルタイプ"""

    ANSWER = 1, "答案用"
    TEST_DATA = 2, "テストデータ用"
    SUBMISSION = 3, "ユーザー提出用"
    DOWNLOAD = 4, "ユーザーダウンロード用"
