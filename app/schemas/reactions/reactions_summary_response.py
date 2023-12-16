from pydantic import Field

from app.schemas.base import PydanticModel


class ReactionsSummaryResponseScout(PydanticModel):
    total_count: int = Field(..., description="総件数")
    send_count: int = Field(..., description="送信数")
    opened_count: int = Field(..., description="開封数")
    opened_rate: float = Field(..., description="開封率")
    agreed_count: int = Field(..., description="承諾数")
    agreed_rate: float = Field(..., description="承諾率")
    replied_count: int = Field(..., description="返信数")
    replied_rate: float = Field(..., description="返信率")


class ReactionsSummaryResponseJob(PydanticModel):
    total_count: int = Field(..., description="総件数")
    viewed_count: int = Field(..., description="開封数")
    applied_count: int = Field(..., description="応募数")
    applied_rate: float = Field(..., description="応募率")


class ReactionsSummaryResponseReactionsReport(PydanticModel):
    scout: ReactionsSummaryResponseScout = Field(..., description="スカウト求人サマリー")
    job: ReactionsSummaryResponseJob = Field(..., description="公開求人サマリー")


class ReactionsSummaryResponse(PydanticModel):
    reaction_summary: ReactionsSummaryResponseReactionsReport = Field(..., description="効果測定サマリー")
