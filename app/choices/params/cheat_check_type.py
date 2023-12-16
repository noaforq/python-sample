from app.choices.base import BaseEnum


class CheatCheckType(str, BaseEnum):
    FOR_TIME = "for_time", "早すぎる解答"
    FOR_MATCH = "for_match", "解答完全一致"
    FOR_SIMILAR = "for_similar", "類似ソースコード"
