from typing import Any

import httpx

from app.configs import settings


async def send_msg_to_slack(text: str, url: str) -> None:
    headers = {"Content-type": "application/json"}
    slack_json = {
        "attachments": [
            {
                "color": "#d74944",
                "fields": [{"value": text}],
            }
        ]
    }
    # 送信する設定でなければコンソール表示のみ
    if not settings.use_slack_web_hooks:
        print(slack_json)
        return

    async with httpx.AsyncClient() as client:
        res = await client.post(url, json=slack_json, headers=headers)
        res.raise_for_status()


# NOTE: 上記send_msg_to_slackではSlack通知の装飾ができないため、以下の関数を新規に用意
async def notify_to_slack(webhook_url: str, attachments: list[dict[str, Any]], /) -> None:
    """Slackに通知を送る

    [usage]
    await notify_to_slack(
        webhook_url,
        [
            {
                "color": color,
                "author_name": author_name,
                "title": title,
                "title_link": title_link,
                "text": text,
                "fields": [{
                    "title": field_title,
                    "value": field_value,
                }]
            }
        ]
    )

    Args:
        webhook_url (str): SlackのWebhook URL
        attachments (list[dict[str, str]]): Slackのattachmentsに渡すパラメータ
    """
    # Slack通知設定がOFFの場合はコンソールに表示して処理を終了する
    if not settings.use_slack_web_hooks:
        print(attachments)
        return

    async with httpx.AsyncClient() as client:
        res = await client.post(webhook_url, json={"attachments": attachments}, headers={"Content-type": "application/json"})
        res.raise_for_status()
