from typing import Any

from app.choices.base import BaseIntEnum


class MessageType(BaseIntEnum):
    MESSAGE_RECEIVED = 1, "メッセージ受信"
    ATTACHMENT_RECEIVED = 2, "ファイル受信"
    AGENT_MESSAGE_RECEIVED = 3, "エージェントからのメッセージ受信"

    # SCOUT
    APPLICATION_APPROVED = 11, "応募承認"
    APPLICATION_REFUSED = 12, "応募拒否"
    AGENT_INTRODUCTION_CREATED = 13, "エージェントからの紹介"
    SELECTION_STEP_CHANGED = 14, "選考ステップ変更"
    APPLICATION_CREATED = 15, "応募"

    # TERM
    TERM_ACCEPTED = 21, "規約承諾"

    # JOB
    JOB_STATUS_CHANGED = 31, "求人ステータス変更"


class BaseMessageChoice(BaseIntEnum):
    @classmethod
    def get_text_label(cls, message_type: MessageType, **kwargs: Any) -> str:
        return cls(message_type, **kwargs).label


class GeneralUserNotificationChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = MessageType.MESSAGE_RECEIVED, "{object_name}から新しいメッセージが届いています。"
    AGENT_MESSAGE_RECEIVED = MessageType.AGENT_MESSAGE_RECEIVED, "エージェントからメッセージが届きました！"
    APPLICATION_APPROVED = (
        MessageType.APPLICATION_APPROVED,
        "{object_name}があなたの求人応募を受け付けました。企業からのメッセージをお待ちください。",
    )
    APPLICATION_REFUSED = MessageType.APPLICATION_REFUSED.value, "{object_name}があなたの求人応募をお断りしました。"
    AGENT_INTRODUCTION_CREATED = (
        MessageType.AGENT_INTRODUCTION_CREATED,
        "{object_name}から{related_name}への求人紹介があります。",
    )
    SELECTION_STEP_CHANGED = MessageType.SELECTION_STEP_CHANGED, "{object_name}の選考ステップが{related_name}になりました。"
    APPLICATION_CREATED = MessageType.APPLICATION_CREATED, "{object_name}の求人 '{related_name}'に応募しました。"


class GeneralUserMailTitleChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = MessageType.MESSAGE_RECEIVED, "[TechFUL] {object_name}から新しいメッセージが届いています。"
    APPLICATION_APPROVED = (
        MessageType.APPLICATION_APPROVED,
        "[TechFUL] {object_name}があなたの求人応募を受け付けました。企業からのメッセージをお待ちください。",
    )
    APPLICATION_REFUSED = MessageType.APPLICATION_REFUSED, "[TechFUL] {object_name}があなたの求人応募をお断りしました。"
    AGENT_MESSAGE_RECEIVED = MessageType.AGENT_MESSAGE_RECEIVED, "[TechFUL] エージェントからメッセージが届きました！"
    AGENT_INTRODUCTION_CREATED = (
        MessageType.AGENT_INTRODUCTION_CREATED,
        "[TechFUL] {object_name}から{related_name}への求人の紹介があります！",
    )
    SELECTION_STEP_CHANGED = MessageType.SELECTION_STEP_CHANGED, "[TechFUL] {object_name}の選考ステップが変更されました。"
    APPLICATION_CREATED = MessageType.APPLICATION_CREATED, "[TechFUL] {object_name}の求人 '{related_name}'に応募しました。"


class GeneralUserMailContentChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = (
        MessageType.MESSAGE_RECEIVED,
        "{username}様\n\n" "{object_name}とのチャットにて、新しいメッセージが届いています。\n\n" "チャットURL: {url_link}\n\n" "本メールへの返信は、転送されませんのでご注意ください。\n\nTechFUL",
    )
    APPLICATION_APPROVED = (
        MessageType.APPLICATION_APPROVED,
        "{username}様\n\n" "{object_name}があなたの求人応募を承諾しました。\n" "メッセージが届くのを待ちましょう！\n\n" "チャットURL: {url_link}\n\n" "TechFUL",
    )
    APPLICATION_REFUSED = (
        MessageType.APPLICATION_REFUSED,
        "{username}様\n\n" "{object_name}があなたの求人応募をお断りしました。\n\n" "他の求人もチェックしてみましょう。\n\n" "求人一覧URL: {url_link}\n\n" "TechFUL",
    )
    AGENT_MESSAGE_RECEIVED = (
        MessageType.AGENT_MESSAGE_RECEIVED,
        "{username}様\n\n" "エージェントからメッセージがきています！\n\n" "下記URLよりサイトにアクセスの上、スカウトの確認をお願いいたします。\n\n" "URL: {url_link}\n\n" "TechFUL",
    )
    AGENT_INTRODUCTION_CREATED = (
        MessageType.AGENT_INTRODUCTION_CREATED,
        "{username}様\n\n" "{object_name}から{related_name}への求人紹介があります！\n\n" "スカウト一覧URL: {url_link}\n\n" "TechFUL",
    )
    SELECTION_STEP_CHANGED = (
        MessageType.SELECTION_STEP_CHANGED,
        "{username}様\n\n" "{object_name}の選考ステップが変更されました。\n\n" "下記URLよりサイトにアクセスの上、確認をお願いいたします。\n\n" "企業名:{object_name}\n" "選考ステップ: {related_name}\n\n" "スカウト一覧URL: {url_link}\n\n" "TechFUL",
    )
    APPLICATION_CREATED = (
        MessageType.APPLICATION_CREATED,
        "{username}様\n\n" "{object_name}の求人\n" "{related_name}に応募しました。\n\n" "スカウト一覧URL: {url_link}\n\n" "TechFUL",
    )


class AgentNotificationChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = MessageType.MESSAGE_RECEIVED, "{username}さんから新しいメッセージが届いています。"
    ATTACHMENT_RECEIVED = MessageType.ATTACHMENT_RECEIVED, "{username}から添付ファイルが届いています。"
    AGENT_INTRODUCTION_CREATED = MessageType.AGENT_INTRODUCTION_CREATED, "{username}さんに{object_name}様の求人を紹介しました"
    SELECTION_STEP_CHANGED = (
        MessageType.SELECTION_STEP_CHANGED,
        "{username}さんの{object_name}様の選考ステップが{related_name}になりました。",
    )
    APPLICATION_CREATED = MessageType.APPLICATION_CREATED, "{username}さんが{object_name}様の{related_name}に求人応募しました。"
    TERM_ACCEPTED = MessageType.TERM_ACCEPTED, "{username}さんが規約を承諾しました。"
    JOB_STATUS_CHANGED = MessageType.JOB_STATUS_CHANGED, "{object_name}様の求人が{status}に変更されました。"


class AgentMailTitleChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = MessageType.MESSAGE_RECEIVED, "[TechFUL] {username}様から新しいメッセージが届いています。"
    ATTACHMENT_RECEIVED = MessageType.ATTACHMENT_RECEIVED, "[TechFUL] {username}から添付ファイルが届いています。"
    AGENT_INTRODUCTION_CREATED = (
        MessageType.AGENT_INTRODUCTION_CREATED,
        "[TechFUL] {username}様に{object_name}様の求人を紹介しました",
    )
    SELECTION_STEP_CHANGED = (MessageType.SELECTION_STEP_CHANGED, "[TechFUL] {username}様の選考ステップが変更されました。")
    APPLICATION_CREATED = MessageType.APPLICATION_CREATED, "[TechFUL] {username}様が{object_name}様の求人に応募しました。"
    TERM_ACCEPTED = MessageType.TERM_ACCEPTED, "[TechFUL] {username}さんが規約を承諾しました。"
    JOB_STATUS_CHANGED = MessageType.JOB_STATUS_CHANGED, "[TechFUL] {object_name}様の求人が{status}に変更されました。"


class AgentMailContentChoice(BaseMessageChoice):
    MESSAGE_RECEIVED = (
        MessageType.MESSAGE_RECEIVED,
        "{agent_name}\n\n" "{username}様とのチャットにて、新しいメッセージが届いています。\n\n" "メッセージ内容:\n" "{message}\n\n" "{url_link}\n\n" "本メールへの返信は、転送されませんのでご注意ください。\n\n" "TechFUL",
    )
    ATTACHMENT_RECEIVED = (
        MessageType.ATTACHMENT_RECEIVED,
        "{agent_name}様\n\n" "{username}とのチャットにて、添付ファイルが届いています。\n\n" "添付ファイル名:\n" "{message}\n\n" "{url_link}\n\n" "本メールへの返信は、転送されませんのでご注意ください。\n\n" "TechFUL",
    )
    AGENT_INTRODUCTION_CREATED = (
        MessageType.AGENT_INTRODUCTION_CREATED,
        "{agent_name}\n\n{username}様に{object_name}様の求人を紹介しました。\n\n{url_link}\n\nTechFUL",
    )
    SELECTION_STEP_CHANGED = (
        MessageType.SELECTION_STEP_CHANGED,
        "{agent_name}\n\n" "{username}様の求人の選考ステップが変更されました。\n\n" "企業名:{object_name}\n" "選考ステップ: {related_name}\n\n" "{url_link}\n\n" "TechFUL",
    )
    APPLICATION_CREATED = (
        MessageType.APPLICATION_CREATED,
        "{agent_name}\n\n{username}様が{object_name}様の求人に応募しました。\n\n{origin}{link}\n\nTechFUL",
    )
    TERM_ACCEPTED = (
        MessageType.TERM_ACCEPTED,
        "{agent_name}\n\n{username}様が規約を承諾しました。\n\n{origin}{link}\n\nTechFUL",
    )
    JOB_STATUS_CHANGED = (
        MessageType.JOB_STATUS_CHANGED,
        "{agent_name}\n\n" "{object_name}様が求人の公開設定を変更しました。\n\n" "企業名:{object_name}\n" "求人名: {related_name}\n" "公開設定: {status}\n\n" "{url_link}\n\n" "TechFUL",
    )
