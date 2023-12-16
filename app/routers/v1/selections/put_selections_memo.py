from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.selections.selections_memo_request_response import SelectionsMemoRequest, SelectionsMemoResponse

router = APIRouter()


@router.put("/{job_id}/{student_id}/memo", response_model=SelectionsMemoResponse, summary="選考メモ更新")
async def put_selections_memo(
    selections_memo: SelectionsMemoRequest,
    job_id: str = Path(..., description="求人ID"),
    student_id: str = Path(..., description="学生ID"),
    session: AsyncSession = Depends(get_session),
) -> SelectionsMemoResponse:
    return SelectionsMemoResponse(memo=selections_memo.memo, job_id=job_id, student_id=student_id)
