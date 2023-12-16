from app.choices.base import BaseIntEnum


class NotificationType(BaseIntEnum):
    """
    通知タイプ
    """

    PERSONAL = 1, "個人"
    ORGANIZATION = 2, "組織"
