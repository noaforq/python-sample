from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.exceptions import NotFound, error_response
from app.models import Company
from app.schemas.companies.companies_contract_request import CompanyContractRequest
from app.schemas.companies.companies_contract_response import CompanyContractResponse

router = APIRouter()


@router.put(
    "/{company_id}/contract",
    summary="スカウト契約更新",
    response_model=CompanyContractResponse,
    responses=error_response(NotFound),
)
async def put_companies_contract(
    contract: CompanyContractRequest,
    company_id: int = Path(..., description="企業ID"),
    session: AsyncSession = Depends(get_session),
) -> dict:
    """スカウト契約を更新する"""

    company = await Company.get_or_none(
        session,
        company_id=company_id,
    )

    if company is None:
        raise NotFound

    contract_dict = contract.dict(exclude_unset=True)
    result = await company.update(session, **contract_dict)

    # TODO user_idを更新用dictに含める or updated_user_idの更新処理を追記する
    # update_user_id =

    # return {
    #     "company_id": company_id,
    #     "contract_expiration_date": contract.contract_expiration_date,
    #     "max_scouts": contract.max_scouts
    # }
    return result
