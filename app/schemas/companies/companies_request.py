from datetime import date

from pydantic import Field

from app.schemas.base import PydanticModel


class CompaniesRequest(PydanticModel):
    max_scouts: int = Field(None, ge=0, description="スカウトを送信できる数")
    contract_expiration_date: date = Field(None, description="スカウトプランの期限が切れる日")
    company_id: int = Field(None, ge=0, description="企業ID")
    name: str = Field(None, description="企業名称")
