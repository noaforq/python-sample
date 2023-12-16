from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.schemas.selections.selections_manage_response import (
    SelectionsManageResponse,
    SelectionsManageResponseSelection,
)

router = APIRouter()


@router.get("/manage", response_model=SelectionsManageResponse, summary="選考管理一覧（企業）")
async def get_selections_manage(page: int | None = None, session: AsyncSession = Depends(get_session)) -> SelectionsManageResponse:
    selection_manage_selection = SelectionsManageResponseSelection(
        job_id="job-id",
        job_title="ABC Inc.",
        student_id="student-id",
        student_fullname="Dohn Joe",
        student_address="Japan",
        student_age=20,
        student_preferred_programming_languages=["C++"],
        student_preferred_frameworks=["BOOST"],
        employment_status=1,
        selection_step=1,
        selection_method=1,
        message_timeline_id="message-timeline-id",
        start_date="2023-10-19T00:00:00Z",
        end_date="2023-10-19T00:00:00Z",
        update_date="2023-10-19T00:00:00Z",
        entry_date="2023-10-19T00:00:00Z",
        last_message_date="2023-10-19T00:00:00Z",
        memo="Nothing",
    )

    return SelectionsManageResponse(total_page=3, current_page=1, selections=[selection_manage_selection])
