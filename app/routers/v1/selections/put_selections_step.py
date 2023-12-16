from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.selections.selections_step_request_response import SelectionsStepRequest, SelectionsStepResponse

router = APIRouter()


@router.put("/{job_id}/{student_id}/step", response_model=SelectionsStepResponse, summary="選考ステップ更新")
async def put_selections_step(
    selections_step: SelectionsStepRequest,
    job_id: str = Path(..., description="求人ID"),
    student_id: str = Path(..., description="学生ID"),
    session: AsyncSession = Depends(get_session),
) -> SelectionsStepResponse:
    return SelectionsStepResponse(selection_step=selections_step.selection_step, job_id=job_id, student_id=student_id)
