from datetime import date, time

from pydantic import Field

from app.schemas.base import PydanticModel


class Areas(PydanticModel):
    area_id: int = Field(..., ge=1, description="エリアID")
    area_name: str = Field(..., description="エリア名")


class Features(PydanticModel):
    feature_id: int = Field(..., ge=1, description="特徴ID")
    feature_name: str = Field(..., description="特徴名")


class ProgrammingLanguages(PydanticModel):
    programming_language_id: int = Field(..., ge=1, description="プログラミング言語ID")
    programming_language_name: str = Field(..., description="プログラミング言語名")


class Frameworks(PydanticModel):
    framework_id: int = Field(..., ge=1, description="フレームワークID")
    framework_name: str = Field(..., description="フレームワーク名")


class Skills(PydanticModel):
    skill_id: int = Field(..., ge=1, description="スキルID")
    skill_name: str = Field(..., description="スキル名")


class Occupation(PydanticModel):
    occupation_id: int = Field(..., ge=1, description="職種ID")
    occupation_name: str = Field(..., description="職種名")


class CommutingTime(PydanticModel):
    commuting_time_from: time = Field(..., description="始業時間")
    commuting_time_to: time = Field(..., description="終業時間")


class Recruitment(PydanticModel):
    recruitment_status: int = Field(..., ge=1, description="募集採用に関する状況")
    recruitment_status_free_input: str = Field(None, description="募集採用に関する状況詳細")


class OccupationalAbility(PydanticModel):
    occupational_ability_status: int = Field(..., ge=1, description="職業能力の開発・向上に関する状況")
    occupational_ability_status_free_input: str = Field(None, description="職業能力の開発・向上に関する状況詳細")


class EmploymentManagement(PydanticModel):
    employment_management_status: int = Field(..., ge=1, description="企業における雇用管理に関して")
    employment_management_status_free_input: str = Field(None, description="企業における雇用管理に関する詳細")


class JobResponse(PydanticModel):
    job_title: str = Field(..., description="求人ポジション名")
    skill_level: int = Field(None, ge=0, description="スキルレベル")
    job_image: str = Field(None, description="求人画像")
    salary_form: int = Field(None, ge=1, description="給与形態")
    min_salary_amount: int = Field(None, description="最小給与額")
    max_salary_amount: int = Field(None, description="最大給与額")
    areas: list[Areas] = Field(None, description="エリア")
    features: list[Features] = Field(None, description="特徴")
    programming_languages: list[ProgrammingLanguages] = Field(None, description="プログラミング言語")
    frameworks: list[Frameworks] = Field(None, description="フレームワーク")
    skills: list[Skills] = Field(None, description="スキル")
    update_at: date = Field(..., description="最終更新日")
    publication_start_date: date = Field(None, description="募集開始日")
    publication_end_date: date = Field(None, description="募集終了日")
    occupation: Occupation = Field(..., description="職種")
    job_description: str = Field(..., description="仕事内容")
    target_people: str = Field(None, description="対象となる方")
    work_location: str = Field(..., description="勤務地")
    number_of_people_hired: int = Field(None, description="採用人数")
    initiatives_to_prevent_passive_smoking: int = Field(..., description="集合場所における受動喫煙防止の取り組み")
    employment_status: int = Field(..., description="雇用形態")
    contract_period: str = Field(..., description="契約期間")
    trial_period: int = Field(..., description="試用期間")
    salary_supplement: str = Field(None, description="給与補足")
    salary_increment: str = Field(None, description="昇給")
    bonus: str = Field(None, description="賞与")
    commuting_time: list[CommutingTime] = Field(None, description="勤務時間")
    commuting_time_supplement: str = Field(None, description="勤務時間補足")
    overtime_work: bool = Field(None, description="時間外勤務")
    overtime_work_free_input: str = Field(None, description="時間外勤務の自由入力")
    holidays_or_vacation: str = Field(None, description="休日・休暇")
    social_insurance: str = Field(..., description="社会保険")
    welfare: str = Field(None, description="福利厚生")
    training_system: str = Field(None, description="研修制度")
    recruitment_flows: list[str] = Field(None, description="採用フロー")
    selection_method: str = Field(None, description="選考方法")
    submitted_document: str = Field(None, description="提出資料")
    recruitment: list[Recruitment] = Field(None, description="募集採用に関する状況に関して")
    occupational_ability: list[OccupationalAbility] = Field(..., description="職業能力の開発・向上に関する状況に関して")
    employment_management: list[EmploymentManagement] = Field(None, description="企業における雇用管理に関して")
    contact_information: str = Field(None, description="	問い合わせ先")
    corporate_pr: str = Field(None, description="企業PR")
    original_content1_title: str = Field(None, description="オリジナルコンテンツ1タイトル")
    original_content1_text: str = Field(None, description="オリジナルコンテンツ1本文")
    original_content2_title: str = Field(None, description="オリジナルコンテンツ2タイトル")
    original_content2_text: str = Field(None, description="オリジナルコンテンツ2本文")
