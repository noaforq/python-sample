import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.common import BaseModel


class Occupations(BaseModel):
    """マスターデータ"""

    __tablename__ = "m_occupations"

    value: Mapped[str] = mapped_column(sqlalchemy.String(32), comment="職種")
