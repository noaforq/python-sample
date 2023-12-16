from app.choices.base import BaseEnum


class FolderConf(str, BaseEnum):
    AT_USER = "user", "ユーザー"
    AT_QUESTION = "question", "問題"
