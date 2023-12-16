from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.exceptions import NotFound, error_response
from app.models import Company
from app.schemas.companies.companies_scout_used_pre_limit_response import CompaniesScoutUsedPreLimitResponse

router = APIRouter()


@router.get(
    "/{company_id}/scout_used_pre_limit",
    summary="スカウト件数取得",
    response_model=CompaniesScoutUsedPreLimitResponse,
    responses=error_response(NotFound),
)
async def get_companies_scout_used_pre_limit(company_id: int = Path(..., description="企業ID"), session: AsyncSession = Depends(get_session)) -> dict:
    """スカウト件数を取得する（使用数/スカウト契約数）"""

    company = await Company.get_or_none(
        session,
        company_id=company_id,
    )

    if company is None:
        raise NotFound

    # TODO スカウト使用数について確認、現状は固定値を返す

    # response = company.dict(exclude_unset=True)
    # response.update(
    #     sent_scout_count = 10
    # )

    # response = CompaniesScoutUsedPreLimitResponse(max_available_scout=0, sent_scout_count=0)
    # return company

    return {"max_scouts": company.max_scouts, "sent_scout_count": 0}
