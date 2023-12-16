from fastapi import APIRouter, Depends, Query

from app.db import AsyncSession, get_session
from app.schemas.jobs.get_jobs_response import GetJobsResponse

router = APIRouter()


@router.get(
    "",
    response_model=GetJobsResponse,
    summary="スカウト求人選択",
)
async def get_jobs(
    job_status: int = Query(..., ge=0, description="求人の状態"),
    session: AsyncSession = Depends(get_session),
) -> GetJobsResponse:
    """スカウト求人を取得する"""

    return {
        "jobs_data": [
            {"job_id": 1, "job_title": "string"},
            {"job_id": 2, "job_title": "string2"},
            {"job_id": 3, "job_title": "string3"},
        ]
    }
