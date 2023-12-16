from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def jst_now() -> datetime:
    return datetime.now(ZoneInfo("Asia/Tokyo"))
