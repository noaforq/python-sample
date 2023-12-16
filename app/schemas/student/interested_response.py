# もっと知りたい送信日用
from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel


class InterestedResponse(PydanticModel):
    send_date: datetime = Field(..., description="送信日")
