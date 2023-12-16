from app.choices.base import BaseEnum


class EventFilter(str, BaseEnum):
    IS_PUBLISHED = "is_published", "公開イベント"
    IS_SPONSOR = "is_sponsor", "協賛イベント"
