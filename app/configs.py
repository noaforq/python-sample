import os
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo

import sqlalchemy
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings

from app.choices.scout.selection_step import SelectionStep

# 本番で使用する固定値は.envに同名で記載することで置き換える


class Settings(BaseSettings):
    secret_key: str = "564f17bfdc9866a42531391f32141a431ff150c99d02b62eb22818d330cfb7a6"
    access_token_expiration_minutes: int = 1440
    refresh_token_expiration_days: int = 15
    password_reset_token_expiration_minutes: int = 60
    signup_token_expiration_minutes: int = 60

    cors_origins: list[str] = ["*"]
    skill_check_key: bytes = b"AAAAABBBBBCCCCCDDDDDEEEEEFFFFFDD"
    server_url: str = "http://127.0.0.1:8000"
    front_url: str = "http://127.0.0.1:3000"
    mock_server_url: str = "http://127.0.0.1:4010"
    judge_server_url: str = "http://127.0.0.1:8080"
    techthon_instance_manager_url: str = "http://127.0.0.1:8144"
    techthon_judge_server_url: str = "https://techthon.techful-api.com"

    show_openapi_docs: bool = True

    db_host: str = "127.0.0.1"
    db_port: int = 1836
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_database: str = "main"
    db_echo: bool = False

    use_cloud_storage: bool = False
    cloud_storage_private_bucket: str = ""
    cloud_storage_public_bucket: str = ""
    cloud_storage_private_judge_bucket: str = ""

    use_email_provider: bool = False  # Falseの場合はコンソールにメール内容出力
    mail_username: str = "apikey"
    mail_password: str = ""
    mail_server: str = "smtp.sendgrid.net"
    mail_port: int = 587
    mail_from: str = "no-reply@techful-programming.com"

    chat_name_444 = "TechFULキャリアアドバイザー"
    chat_logo_444 = ""
    chat_file_download_url_expiration_minutes = 1

    use_slack_web_hooks: bool = False
    enabled_profiler: bool = False
    profiler_verbose: int = 3

    # STG向けslack_hooksのURL （envには本番用チャンネルを記載すること）
    slack_url_for_judge_err: str = "https://hooks.slack.com/services/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"
    slack_url_for_job_script: str = "https://hooks.slack.com/services/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"
    slack_url_for_school_user_registration: str = "https://hooks.slack.com/services/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"
    # 学校登録時のslack通知先
    slack_url_for_create_school: str = "https://hooks.slack.com/services/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"
    # 学部・学科登録時のslack通知先
    slack_url_for_create_school_department: str = "https://hooks.slack.com/services/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"
    # 学校アカウント登録時のslack通知先
    slack_url_for_create_school_user: str = "https://hooks.slack.com/services/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"
    # 求人原稿掲載終了前通知のSlack通知先
    slack_url_for_job_expiration_notice: str = "https://hooks.slack.com/services/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"
    # 444側へのslack通知メール
    email_to_444_agent: str = "t4c6w5v6j8v7j2h7@triple-four.slack.com"
    email_to_444_staff: str = "s8k4z7e2t0f1u0h9@triple-four.slack.com"
    # 444側への選考ステップ変更通知メール
    email_to_444_agent_status: str = "o8p7q7u6u4j7x6o8@triple-four.slack.com"
    # 444側への求人紹介通知
    email_to_444_agent_intro: str = "j0h4v2i2g8i5p5c3@triple-four.slack.com"
    # スタッフが問題公開情報を更新した時の社内通知先
    email_update_questions_publish: str = "a6a9b4i4k6b6b5b3@triple-four.slack.com"

    # 問い合わせ送信先
    contact_recipient: str = "d8i1o4l5h1k9q1i9@triple-four.slack.com"

    # 認証情報をキャッシュするためのRedis
    authentication_cache_redis_host_name: str = "redis"
    authentication_cache_redis_port: int = 283
    authentication_cache_db_index: int = 0

    # ユーザ情報をキャッシュするためのRedis
    user_identity_cache_redis_host_name: str = "redis"
    user_identity_cache_redis_port: int = 283
    user_identity_cache_db_index: int = 1

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

BASE_DIR: str = str(Path(__file__).resolve().parent.parent)

STATIC_DIR: str = "static"
STATIC_URL: str = "static"

JWT_ALGORITHM: str = "HS256"

DB_URL = sqlalchemy.engine.url.URL.create(
    drivername="postgresql+asyncpg",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_database,
)

email_conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=BASE_DIR + "/app/resources/email_template",
)

PASSWORD_RESET_URL: str = settings.front_url + "/account/password-reset/form/{token}"
EMAIL_UPDATE_URL: str = settings.front_url + "/techful/account/mail/complete/{token}"
SUB_EMAIL_UPDATE_URL: str = f"{EMAIL_UPDATE_URL}?is_sub_email=true"
SIGNUP_URL: str = settings.front_url + "/account/register/complete/{token}"
JUDGE_URL: str = settings.judge_server_url + "/judge/judge"
JUDGE_RESULT_URL: str = settings.server_url + "/judge/results"
JUDGE_TEST_CASE_URL: str = settings.judge_server_url + "/testcase/test-case-data"
TECHTHON_INSTANCE_CREATION_URL: str = settings.techthon_instance_manager_url + "/instance/create"  # POST
TECHTHON_INSTANCE_BULK_CREATION_URL: str = settings.techthon_instance_manager_url + "/instance/bulk-create"  # POST
TECHTHON_INSTANCE_TERMINATION_URL: str = settings.techthon_instance_manager_url + "/instance/bulk-stop"  # DELETE
TECHTHON_INSTANCE_REBOOT_URL: str = settings.techthon_instance_manager_url + "/instance/reboot"  # PATCH


TECHTHON_JUDGE_URL: str = settings.techthon_judge_server_url + "/api/techthon/response_check"

TECHTHON_JUDGE_TIMEOUT: int = 2


CHAT_GENERAL_URL: str = settings.front_url + "/techful/chat?room={room_id}"
CHAT_MANAGE_STAFF_URL: str = settings.front_url + "/staff/chat?room={room_id}"
CHAT_MANAGE_COMPANY_URL: str = settings.front_url + "/company/chat?room={room_id}"
CHAT_MANAGE_SCHOOL_URL: str = settings.front_url + "/school/chat?room={room_id}"

EMAIL_TO_444_AGENT: str = settings.email_to_444_agent
EMAIL_TO_444_STAFF: str = settings.email_to_444_staff
EMAIL_TO_444_AGENT_STATUS: str = settings.email_to_444_agent_status
EMAIL_TO_444_AGENT_INTRO: str = settings.email_to_444_agent_intro

CONTACT_RECIPIENT: str = settings.contact_recipient

LOGIN_URL: str = settings.front_url + "/account/login"
SELECTION_GENERAL_URL: str = settings.front_url + "/techful/job/scout"
SELECTION_MANAGE_URL: str = settings.front_url + "/staff/screening?company_id={company_id}"
JOB_URL: str = settings.front_url + "/techful/job/{job_id}"

JAPAN_TZ = ZoneInfo("Asia/Tokyo")


SLACK_URL_FOR_JUDGE_ERR: str = settings.slack_url_for_judge_err
SLACK_URL_FOR_JOB_SCRIPT: str = settings.slack_url_for_job_script

JOB_STAFF_URL: str = settings.front_url + "/staff/job/{job_id}"
JOB_DRAFT_STAFF_URL: str = settings.front_url + "/staff/job/draft/{draft_id}"
JOB_STAFF_URL_FOR_COMPANY_HR: str = settings.front_url + "/staff/company-hr/{organization_id}/job/{job_id}"
JOB_DRAFT_STAFF_URL_FOR_COMPANY_HR: str = settings.front_url + "/staff/company-hr/{organization_id}/job/{job_draft_id}/draft"

# アクセスログのミドルウェアの設定のために追加
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")  # ローカルではこの環境変数を設定しないこと
LOG_NAME = "access-log"

# 444株式会社の組織ID
ORG_444_ID = 1

# トライアルのプロパティID
IS_TRIAL_SKILL_EVALUATION = "is_trial_skill_evaluation"
IS_TRIAL_SCOUT = "is_trial_scout"

# 書類選考以降のステップ
SELECTION_STEP_LIST = [
    SelectionStep.DOCUMENT_SCREENING,
    SelectionStep.FIRST_SELECTION,
    SelectionStep.SECOND_SELECTION,
    SelectionStep.THIRD_SELECTION,
    SelectionStep.FOURTH_SELECTION,
    SelectionStep.FIFTH_SELECTION,
    SelectionStep.UNOFFICIAL_OFFER,
    SelectionStep.ACCEPTED_UNOFFICIAL_OFFER,
    SelectionStep.HIRED,
]
