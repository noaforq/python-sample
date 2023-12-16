from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session

router = APIRouter()


@router.post(
    "/{company_id}/accept_terms",
    summary="スカウトの利用規約承諾",
    # responses=error_response(ValidationError),
)
async def post_companies_accept_terms(
    company_id: int = Path(False, description="企業ID"),
    session: AsyncSession = Depends(get_session),
) -> None:
    """スカウトの利用規約承諾時に１度だけ使用する"""
    # ロジック部分は後ほど記述

    if not company_id:
        # TODO: エラー処理にする
        pass

    return
