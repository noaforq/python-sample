from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.selections.selections_request_response import SelectionsJobIdStudentIdResponse, SelectionsRequest

router = APIRouter()


@router.post("/{job_id}/{student_id}", response_model=SelectionsJobIdStudentIdResponse, summary="スカウト送信")
async def post_selections(
    selections_request: SelectionsRequest,
    job_id: str = Path(..., description="求人ID"),
    student_id: str = Path(..., description="学生ID"),
    session: AsyncSession = Depends(get_session),
) -> SelectionsJobIdStudentIdResponse:
    return SelectionsJobIdStudentIdResponse(
        create_at="2023-10-19T00:00:00Z",
        job_id="job-id",
        student_id="student-id",
    )
