from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsMemoRequest(PydanticModel):
    memo: str = Field(..., description="メモの中身")


class SelectionsMemoResponse(PydanticModel):
    memo: str = Field(..., description="更新後のメモの中身")
    job_id: int = Field(..., description="選考ID")
    student_id: int = Field(..., description="学生ID")
