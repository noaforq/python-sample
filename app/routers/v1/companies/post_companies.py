from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.models import Company
from app.schemas.companies.companies_request import CompaniesRequest

router = APIRouter()


@router.post("", response_model=None, summary="スカウト契約連携", status_code=201)
async def post_companies(companies: CompaniesRequest, session: AsyncSession = Depends(get_session)) -> dict:
    """スカウト契約をスカウトに連携する"""

    insert_dict = companies.dict(exclude_unset=True)
    insert_dict.update(
        created_user_id=5,
        updated_user_id=5,
    )

    await Company.create(session, **insert_dict)

    # return result
    return {}
