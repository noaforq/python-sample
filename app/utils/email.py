from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import validator

from app.configs import email_conf, settings
from app.models.users.user_common_info import UserCommonInfo


class CustomMessageSchema(MessageSchema):
    @validator("subtype")
    def validate_subtype(cls, value, values, config, field):  # type: ignore # NOQA
        """validator上書き"""
        return value


async def send_email_to_user(
    user_common_info: UserCommonInfo,
    subject: str,
    body: str | None = None,
    template_name: str | None = None,
    template_body: dict | None = None,
    subtype: MessageType = MessageType.plain,
) -> None:
    """
    user_common_info に設定されたメアドにメールを送信する。
    sub_email が登録されていればそちらにも送信する。
    """
    recipients = [user_common_info.email]
    if sub_email := user_common_info.sub_email:
        recipients.append(sub_email)

    return await send_email(
        subject=subject,
        recipients=recipients,
        body=body,
        template_name=template_name,
        template_body=template_body,
        subtype=subtype,
    )


async def send_email(
    subject: str,
    recipients: list[str] | str,
    body: str | None = None,
    template_name: str | None = None,
    template_body: dict | None = None,
    subtype: MessageType = MessageType.plain,
) -> None:

    if isinstance(recipients, str):
        recipients = [recipients]

    message = CustomMessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype=subtype,
        template_body=template_body,
    )

    fm = FastMail(email_conf)

    # メール送信しない場合コンソールに表示
    if not settings.use_email_provider:
        if template_name:
            template = await fm.get_mail_template(fm.config.template_engine(), template_name)
            msg = template.render(template_body)
        else:
            msg = body
        print(
            "~" * 100,
            f"subject:{subject}",
            f"recipients:{recipients}",
            "-" * 100,
            msg,
            "~" * 100,
            sep="\n",
        )
        return

    await fm.send_message(message, template_name)
