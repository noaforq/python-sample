from fastapi import APIRouter, Depends, Path, Query

from app.db import AsyncSession, get_session
from app.schemas.jobs.get_jobs_pages_response import GetJobsResponse

router = APIRouter()


@router.get(
    "/pages/{page}",
    response_model=GetJobsResponse,
    summary="スカウト求人取得",
)
async def get_jobs_pages(
    page: int = Path(1, ge=1),
    job_status: int = Query(None, ge=0, description="求人の状態"),
    session: AsyncSession = Depends(get_session),
) -> GetJobsResponse:
    """スカウト求人の一覧を取得する（指定のページ）"""

    print(page)
    return {
        "todal_page": 3,
        "current_page": 1,
        "jobs_data": [
            {
                "job_title": "string1",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 0,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string2",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 10,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string3",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 20,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string4",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 25,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string5",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 30,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string6",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 40,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string7",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 50,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string8",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 90,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string9",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 0,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
            {
                "job_title": "string10",
                "graduation_year": 0,
                "employment_status": 1,
                "skill_level": 0,
                "status": 0,
                "created_at": "2019-08-24T04:05:06Z",
                "updated_at": "2019-08-25T04:05:06Z",
            },
        ],
    }
