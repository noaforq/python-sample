from pydantic import Field

from app.schemas.base import PydanticModel


class ReactionsAppliedRequest(PydanticModel):
    student_id: str = Field(..., description="生徒ID")
