from pydantic import Field

from app.schemas.base import PydanticModel


class ReactionsResponseScout(PydanticModel):
    send_count: int = Field(..., description="送信数")
    opened_count: int = Field(..., description="開封数")
    opened_rate: float = Field(..., description="開封率")
    agreed_count: int = Field(..., description="承諾数")
    agreed_rate: float = Field(..., description="承諾率")
    replied_count: int = Field(..., description="返信数")
    replied_rate: float = Field(..., description="返信率")


class ReactionsResponseJob(PydanticModel):
    viewed_count: int = Field(..., description="開封数")
    applied_count: int = Field(..., description="応募数")
    applied_rate: float = Field(..., description="応募率")


class ReactionsResponseReactionsReport(PydanticModel):
    scout: ReactionsResponseScout = Field(..., description="スカウト効果測定")
    job: ReactionsResponseJob = Field(..., description="公開求人効果測定。求人を公開していない場合はnullになる")
    start_date: str = Field(..., description="求人開始日")
    position_name: str = Field(..., description="ポジション名")


class ReactionsResponse(PydanticModel):
    reactions_reports: list[ReactionsResponseReactionsReport] = Field(..., description="各スカウト・求人の効果測定で、配列の項目1個が1つの求人に対応する。求人がない場合は空配列になる")
