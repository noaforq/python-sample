from typing import Any

from fastapi import status


class BaseAPIException(Exception):
    status_code: int
    error_code: str = ""
    headers: dict | None = None
    default_detail: Any = ""
    default_message: str = ""

    def __init__(self, detail: Any = None, message: str | None = None) -> None:
        self.detail = self.default_detail
        self.message = self.default_message
        if detail:
            self.detail = detail
        if message:
            self.message = message


# 400
class CannotBeDeleted(BaseAPIException):
    """データが紐付いているため削除不可"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "CANNOT_BE_DELETED"
    default_detail = "Cannot be deleted because the data is linked"
    default_message = "データが紐付いているため削除できません"


class CannotBeExecutedConditionsNotSatisfied(BaseAPIException):
    """条件を満たしていないため実行不可"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "CANNOT_EXECUTED_CONDITIONS_NOT_SATISFIED"
    default_detail = "Cannot be executed because the required conditions are not satisfied."
    default_message = "条件を満たしていないため実行不可"


class DataDoesNotExist(BaseAPIException):
    """存在しないデータを参照している"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "DATA_DOES_NOT_EXIST"
    default_detail = "Data with the specified ID does not exist"
    default_message = "指定されたIDのデータは存在しません"


class ParameterError(BaseAPIException):
    """パラメータが不正"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "PARAMETER_ERROR"
    default_detail = "Parameter error"
    default_message = "指定されたパラメータは不正です"


class AlreadyExistsUsernameOrEmail(BaseAPIException):
    """同じユーザー名またはメールアドレスがすでに登録済み"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "ALREADY_EXISTS_USERNAME_OR_EMAIL"
    default_detail = ["username", "email"]
    default_message = "同じユーザー名またはメールアドレスがすでに登録済みです"


class AlreadyExistsEmail(BaseAPIException):
    """同じメールアドレスがすでに登録済み"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "ALREADY_EXISTS_EMAIL"
    default_detail = "Already Exists Email"
    default_message = "同じメールアドレスがすでに登録済みです"


class AlreadyLinkedMoodle(BaseAPIException):
    """既にMoodle連携済み"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "ALREADY_LINKED_MOODLE"
    default_detail = "Already Linked Moodle"
    default_message = "既にMoodle連携済みです"


class DuplicateError(BaseAPIException):
    """データが重複している"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "DUPLICATE_ERROR"
    default_detail = "duplicate key value violates unique constraintr"
    default_message = "データが重複しています"


class QuestionAnswerNotStarted(BaseAPIException):
    """問題解答開始していない"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "QUESTION_ANSWER_NOT_STARTED"
    default_detail = "question answer not started"
    default_message = "問題解答開始していないため実行できません"


class InactiveSessionError(BaseAPIException):
    """セッションが一時停止中"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "INACTIVE_SESSION_ERROR"
    default_detail = "session is inactive now"
    default_message = "セッションは一時停止中のため実行できません"


class LittleTestSessionReanswer(BaseAPIException):
    """小テストセッションは再解答不可"""

    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "LITTLE_TEST_SESSION_REANSWER"
    default_detail = "little test session reanswer"
    default_message = "小テストセッションのため再解答できません"


# 401
class IncorrectUsernameOrPassword(BaseAPIException):
    """ユーザー名またはパスワードが不正"""

    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INCORRECT_USERNAME_OR_PASSWORD"
    default_detail = "Incorrect username or password"
    default_message = "ユーザー名またはパスワードが不正です"


class InvalidRefreshToken(BaseAPIException):
    """リフレッシュトークンが不正"""

    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INVALID_REFRESH_TOKEN"
    default_detail = "invalid refresh token"
    default_message = "認証情報が無効です"


class InvalidCredentials(BaseAPIException):
    """アクセストークンが不正、または有効期限切れ"""

    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INVALID_CREDENTIALS"
    default_detail = "invalid credentials"
    default_message = "認証情報が無効です"
    headers = {"WWW-Authenticate": "Bearer"}


class DoesNotBelongToAnyTechthonTeam(BaseAPIException):
    """Techthonチームに所属していない"""

    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "DOES_NOT_BELONG_TO_ANY_TECHTHON_TEAM"
    default_detail = "does not belong to any techthon team"
    default_message = "Techthonチームに所属していません"


# 403
class PermissionDenied(BaseAPIException):
    """APIを実行する権限がない"""

    status_code = status.HTTP_403_FORBIDDEN
    error_code = "PERMISSION_DENIED"
    default_detail = "permission denied"
    default_message = "実行する権限がありません"


# 404
class NotFound(BaseAPIException):
    """指定したIDのデータが存在しない"""

    status_code = status.HTTP_404_NOT_FOUND
    error_code = "NOT_FOUND"
    default_detail = "not found"
    default_message = "データが存在しません"


# 422
class FilenameLengthMaxExceeded(BaseAPIException):
    """ファイル名の文字数が上限を超えている"""

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    error_code = "FILENAME_LENGTH_MAX_EXCEEDED"
    default_detail = "filename length max exceeded"
    default_message = "ファイル名の文字数が上限を超えています"


# 500
class InternalServerError(BaseAPIException):
    """サーバーエラーが発生"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_code = "INTERNAL_SERVER_ERROR"
    default_detail = "internal server error"
    default_message = "エラーが発生しました"
