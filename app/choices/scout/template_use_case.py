from app.choices.base import BaseIntEnum


class TemplateUseCase(BaseIntEnum):
    """
    テンプレート/用途
    """

    SCOUT_TEMPLATE = 1, "スカウトテンプレート"
    MESSAGE_TEMPLATE = 2, "メッセージテンプレート"
