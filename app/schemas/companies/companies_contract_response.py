from datetime import date

from pydantic import Field

from app.schemas.base import PydanticModel


class CompanyContractResponse(PydanticModel):
    name: str = Field(..., description="企業名")
    contract_expiration_date: date = Field(..., description="スカウトプランの期限が切れる日")
    max_scouts: int = Field(..., description="スカウトを送信できる数")
