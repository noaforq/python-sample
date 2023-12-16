from pydantic import Field

from app.schemas.base import PydanticModel


class OccupationList(PydanticModel):
    occupation_id: int | None = Field(None, ge=1, description="職種ID")
    occupation_name: str = Field(default="", description="職種名")


class ProgrammingLanguageList(PydanticModel):
    programming_language_id: int | None = Field(None, ge=1, description="プログラミング言語ID")
    programming_language_name: str = Field(default="", description="プログラミング言語名")


class FrameworkList(PydanticModel):
    framework_id: int | None = Field(None, ge=1, description="フレームワークID")
    framework_name: str = Field(default="", description="フレームワーク名")


class SkillList(PydanticModel):
    skill_id: int | None = Field(None, ge=1, description="スキルID")
    skill_name: str = Field(default="", description="スキル名")


class FeatureList(PydanticModel):
    feature_id: int | None = Field(None, ge=1, description="特徴ID")
    feature_name: str = Field(default="", description="特徴名")


class AreaList(PydanticModel):
    area_id: int | None = Field(None, ge=1, description="エリアID")
    area_name: str = Field(default="", description="エリア名")


class IndustryList(PydanticModel):
    industry_id: int | None = Field(None, ge=1, description="業種ID")
    industry_name: str = Field(default="", description="業種名")


class SchoolList(PydanticModel):
    school_id: int | None = Field(None, ge=1, description="学校ID")
    school_name: str = Field(default="", description="学校名")


class FacultyList(PydanticModel):
    faculty_id: int | None = Field(None, ge=1, description="学部ID")
    faculty_name: str = Field(default="", description="学部名")


class QualificationList(PydanticModel):
    qualification_id: int | None = Field(None, ge=1, description="資格ID")
    qualification_name: str = Field(default="", description="資格名")


class ProgrammingExperienceList(PydanticModel):
    programming_experience_id: int | None = Field(None, ge=1, description="プログラミング経験ID")
    programming_experience_name: str = Field(default="", description="プログラミング経験名")


class MasterResponse(PydanticModel):
    occupations: list[OccupationList] | None
    programming_languages: list[ProgrammingLanguageList] | None
    frameworks: list[FrameworkList] | None
    skills: list[SkillList] | None
    features: list[FeatureList] | None
    areas: list[AreaList] | None
    industries: list[IndustryList] | None
    schools: list[SchoolList] | None
    faculties: list[FacultyList] | None
    qualification: list[QualificationList] | None
    programming_experience: list[ProgrammingExperienceList] | None
