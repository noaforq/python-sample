from pydantic import Field

from app.schemas.base import PydanticModel


class CompaniesScoutUsedPreLimitResponse(PydanticModel):
    max_scouts: int = Field(..., description="送信可能なスカウト数")
    sent_scout_count: int = Field(..., description="送信したスカウト数")
