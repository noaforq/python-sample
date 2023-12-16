from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsRequest(PydanticModel):
    message: str = Field(..., description="リクエストボディ")


class SelectionsJobIdStudentIdResponse(PydanticModel):
    create_at: str = Field(..., description="スカウト送信キューへの追加日時")
    job_id: str = Field(..., description="選考ID")
    student_id: str = Field(..., description="学生ID")
