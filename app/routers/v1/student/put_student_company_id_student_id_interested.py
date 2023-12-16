from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.student.interested_response import InterestedResponse

router = APIRouter()


@router.put(
    "/{company_id}/{student_id}/interested",
    response_model=InterestedResponse,
    summary="もっと知りたい最終送信日更新",
)
async def put_student_company_id_student_id_interested(
    company_id: str = Path(...),
    student_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
) -> InterestedResponse:
    """「もっと知りたい」の最終送信日を更新する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()
    return InterestedResponse(send_date="2019-08-24T14:15:22Z")
