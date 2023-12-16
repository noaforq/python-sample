from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.selections.selections_scheduled_date_request_response import (
    SelectionsScheduledDateRequest,
    SelectionsScheduledDateResponse,
)

router = APIRouter()


@router.put("/{job_id}/{student_id}/scheduled_date", response_model=SelectionsScheduledDateResponse, summary="選考予定日更新")
async def put_selections_scheduled_date(
    selections_scheduled_date: SelectionsScheduledDateRequest,
    job_id: str = Path(..., description="求人ID"),
    student_id: str = Path(..., description="学生ID"),
    session: AsyncSession = Depends(get_session),
) -> SelectionsScheduledDateResponse:
    return SelectionsScheduledDateResponse(
        scheduled_start_date=selections_scheduled_date.scheduled_start_date,
        scheduled_end_date=selections_scheduled_date.scheduled_end_date,
        job_id=job_id,
        student_id=student_id,
    )
