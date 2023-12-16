from pydantic import Field

from app.schemas.base import PydanticModel


class MasterOccupationsResponse(PydanticModel):
    value: str = Field(None, description="職種")
