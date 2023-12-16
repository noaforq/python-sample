from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsStepRequest(PydanticModel):
    selection_step: int = Field(..., description="選考ステップ")


class SelectionsStepResponse(PydanticModel):
    selection_step: int = Field(..., description="更新後の選考ステップ")
    job_id: int = Field(..., description="選考ID")
    student_id: int = Field(..., description="学生ID")
