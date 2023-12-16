from datetime import date

from fastapi import APIRouter, Depends, Path
from pydantic import BaseModel, Field

from app.db import AsyncSession, get_session
from app.schemas.jobs.job_response import (
    Areas,
    CommutingTime,
    EmploymentManagement,
    Features,
    Frameworks,
    JobResponse,
    Occupation,
    OccupationalAbility,
    ProgrammingLanguages,
    Recruitment,
    Skills,
)

router = APIRouter()


class Job(BaseModel):
    is_use_published_job: bool = Field(..., description="公開求人にするか否か")
    publication_start_date: date = Field(..., description="募集開始日")
    publication_end_date: date = Field(..., description="募集終了日")
    employment_status: int = Field(..., ge=1, description="雇用形態")
    graduation_year: int = Field(None, ge=0, description="対象年度")
    occupation: int = Field(..., description="職種")
    initiatives_to_prevent_passive_smoking: int = Field(..., ge=1, description="集合場所における受動喫煙防止の取り組み")
    number_of_people_hired: int = Field(None, ge=0, description="採用人数")
    skill_level: int = Field(None, ge=0, description="スキルレベル")
    programming_languages: list[int] = Field(None, ge=1, description="プログラミング言語")
    frameworks: list[int] = Field(None, ge=1, description="フレームワーク")
    skills: list[int] = Field(None, ge=1, description="スキル")
    features: list[int] = Field(None, ge=1, description="特徴")
    areas: list[int] = Field(None, ge=1, description="エリア")
    salary_form: int = Field(None, ge=1, description="給与形態")
    min_salary_amount: int = Field(None, ge=0, description="最小給与額")
    max_salary_amount: int = Field(None, ge=0, description="最大給与額")
    salary_supplement: str = Field(None, description="給与補足")
    commuting_time: list[CommutingTime] = Field(..., description="勤務時間")
    job_title: str = Field(..., description="求人名")
    job_image: str = Field(None, description="求人画像")
    job_description: str = Field(..., description="仕事内容")
    target_people: str = Field(None, description="対象となる方")
    work_location: str = Field(..., description="勤務地")
    contract_period: str = Field(..., description="契約期間")
    trial_period: int = Field(..., ge=0, description="試用期間")
    salary_increment: str = Field(None, description="昇給")
    bonus: str = Field(None, description="賞与")
    commuting_time_supplement: str = Field(None, description="勤務時間補足")
    overtime_work: bool = Field(None, description="時間外勤務")
    overtime_work_free_input: str = Field(None, description="時間外勤務の自由入力")
    holidays_or_vacation: str = Field(None, description="休日・休暇")
    social_insurance: str = Field(..., description="社会保険")
    welfare: str = Field(..., description="福利厚生")
    training_system: str = Field(None, description="研修制度")
    recruitment_flows: list[str] = Field(None, description="採用フロー")
    selection_method: str = Field(None, description="選考方法")
    submitted_document: str = Field(None, description="提出資料")
    recruitment: list[Recruitment] = Field(None, description="募集採用に関する状況に関して")
    occupational_ability: list[OccupationalAbility] = Field(None, description="職業能力の開発・向上に関する状況に関して")
    employment_management: list[EmploymentManagement] = Field(None, description="企業における雇用管理に関して")
    contact_information: str = Field(None, description="問い合わせ先")
    corporate_pr: str = Field(None, description="企業PR")
    original_content1_title: str = Field(None, description="オリジナルコンテンツ1タイトル")
    original_content1_text: str = Field(None, description="オリジナルコンテンツ1本文")
    original_content2_title: str = Field(None, description="オリジナルコンテンツ2タイトル")
    original_content2_text: str = Field(None, description="オリジナルコンテンツ2本文")


@router.put(
    "/{job_id}",
    response_model=JobResponse,
    summary="スカウト求人更新",
)
async def put_jobs(
    job: Job,
    job_id: int = Path(..., ge=1, description="求人ID"),
    session: AsyncSession = Depends(get_session),
) -> JobResponse:
    """スカウト求人を更新する"""
    if job.occupation:
        job_occupation = Occupation(occupation_id=job.occupation, occupation_name="string")

    area_list = []
    if job.areas:
        for area in job.areas:
            jobs_areas = Areas(area_id=area, area_name="string")
            area_list.append(jobs_areas)

    feature_list = []
    if job.features:
        for feature in job.features:
            jobs_feature = Features(feature_id=feature, feature_name="string")
            feature_list.append(jobs_feature)

    programming_language_list = []
    if job.programming_languages:
        for pl_id in job.programming_languages:
            jobs_programming_language = ProgrammingLanguages(programming_language_id=pl_id, programming_language_name="string")
            programming_language_list.append(jobs_programming_language)

    framework_list = []
    if job.frameworks:
        for framework in job.frameworks:
            jobs_framework = Frameworks(framework_id=framework, framework_name="string")
            framework_list.append(jobs_framework)

    skill_list = []
    if job.skills:
        for skill in job.skills:
            jobs_skill = Skills(skill_id=skill, skill_name="string")
            skill_list.append(jobs_skill)

    result = JobResponse(
        job_id=job_id,
        publication_start_date=job.publication_start_date,
        publication_end_date=job.publication_end_date,
        employment_status=job.employment_status,
        occupation=job_occupation,
        initiatives_to_prevent_passive_smoking=job.initiatives_to_prevent_passive_smoking,
        number_of_people_hired=job.number_of_people_hired if job.number_of_people_hired else None,
        skill_level=job.skill_level if job.skill_level else None,
        programming_languages=programming_language_list,
        frameworks=framework_list,
        skills=skill_list,
        features=feature_list,
        areas=area_list,
        salary_form=job.salary_form if job.salary_form else None,
        min_salary_amount=job.min_salary_amount if job.min_salary_amount else None,
        max_salary_amount=job.max_salary_amount if job.max_salary_amount else None,
        salary_supplement=job.salary_supplement if job.salary_supplement else None,
        commuting_time=job.commuting_time,
        job_title=job.job_title,
        job_image=job.job_image if job.job_image else None,
        job_description=job.job_description,
        target_people=job.target_people if job.target_people else None,
        work_location=job.work_location,
        contract_period=job.contract_period,
        trial_period=job.trial_period,
        salary_increment=job.salary_increment if job.salary_increment else None,
        bonus=job.bonus if job.bonus else None,
        commuting_time_supplement=job.commuting_time_supplement if job.commuting_time_supplement else None,
        overtime_work=job.overtime_work if job.overtime_work else None,
        overtime_work_free_input=job.overtime_work_free_input if job.overtime_work_free_input else None,
        holidays_or_vacation=job.holidays_or_vacation if job.holidays_or_vacation else None,
        social_insurance=job.social_insurance,
        welfare=job.welfare,
        training_system=job.training_system if job.training_system else None,
        recruitment_flows=job.recruitment_flows if job.recruitment_flows else None,
        selection_method=job.selection_method if job.selection_method else None,
        submitted_document=job.submitted_document if job.submitted_document else None,
        recruitment=job.recruitment if job.recruitment else None,
        occupational_ability=job.occupational_ability if job.occupational_ability else None,
        employment_management=job.employment_management if job.employment_management else None,
        contact_information=job.contact_information if job.contact_information else None,
        corporate_pr=job.corporate_pr if job.corporate_pr else None,
        original_content1_title=job.original_content1_title if job.original_content1_title else None,
        original_content1_text=job.original_content1_text if job.original_content1_text else None,
        original_content2_title=job.original_content2_title if job.original_content2_title else None,
        original_content2_text=job.original_content2_text if job.original_content2_text else None,
        update_at=date.today(),
    )

    return result
