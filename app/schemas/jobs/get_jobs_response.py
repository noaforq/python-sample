from pydantic import Field

from app.schemas.base import PydanticModel


class JobsData(PydanticModel):
    job_id: int = Field(..., ge=1, description="求人ID")
    job_title: str = Field(..., description="求人名")


class GetJobsResponse(PydanticModel):
    jobs_data: list[JobsData] | None
