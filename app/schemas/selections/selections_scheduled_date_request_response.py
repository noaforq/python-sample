from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsScheduledDateRequest(PydanticModel):
    scheduled_start_date: str = Field(..., description="選考開始日")
    scheduled_end_date: str = Field(..., description="選考終了日")


class SelectionsScheduledDateResponse(PydanticModel):
    scheduled_start_date: str = Field(..., description="更新後の選考開始日")
    scheduled_end_date: str = Field(..., description="更新後の選考終了日")
    job_id: int = Field(..., description="選考ID")
    student_id: int = Field(..., description="学生ID")
