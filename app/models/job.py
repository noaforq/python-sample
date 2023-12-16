from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import (
        Company,
        ProgrammingLanguage,
        Framework,
        Skill,
        FavoriteJob,
        Feature,
        Area,
        CommutingTime,
        RecruitmentFlow,
        RecruitmentStatus,
        OccupationalAbilityStatus,
        EmploymentManagementStatus,
        JobTemplate,
        Reaction,
        Selection,
    )

from app.choices.scout import (
    EmploymentStatus,
    InitiativesToPreventPassiveSmoking,
    SalaryForm,
    SkillLevel,
    Status,
    TrialPeriod,
)
from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum


class Job(TransactionBase):
    """求人"""

    __tablename__ = "jobs"

    company_id: Mapped[str] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    status: Mapped[Status] = mapped_column(IntEnum(Status), index=True, comment="状態")
    applied_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="申請日時")
    is_use_published_job: Mapped[bool] = mapped_column(sa.Boolean(True), comment="公開求人にするか否か")
    publication_start_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="掲載開始")
    publication_end_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="掲載終了")
    employment_status: Mapped[EmploymentStatus] = mapped_column(IntEnum(EmploymentStatus), comment="雇用形態")
    graduation_year: Mapped[int] = mapped_column(sa.Integer(), comment="卒業年")
    m_occupation_id: Mapped[int] = mapped_column(sa.Integer(), comment="職種")
    number_of_people_hired: Mapped[int] = mapped_column(sa.Integer(), comment="採用人数")
    initiatives_to_prevent_passive_smoking: Mapped[InitiativesToPreventPassiveSmoking] = mapped_column(IntEnum(InitiativesToPreventPassiveSmoking), comment="就業場所における受動喫煙防止の取組")
    skill_level: Mapped[SkillLevel] = mapped_column(IntEnum(SkillLevel), comment="スキルレベル")
    salary_form: Mapped[SalaryForm] = mapped_column(IntEnum(SalaryForm), comment="給与形態")
    min_salary_amount: Mapped[int] = mapped_column(sa.Integer(), comment="最小給与額")
    max_salary_amount: Mapped[int] = mapped_column(sa.Integer(), comment="最大給与額")
    salary_supplement: Mapped[str] = mapped_column(sa.String(255), comment="給与補足")
    commuting_time_supplement: Mapped[str] = mapped_column(sa.String(255), comment="勤務時間補足")
    job_title: Mapped[str] = mapped_column(sa.String(63), comment="求人タイトル")
    job_image: Mapped[str] = mapped_column(sa.String(255), comment="求人トップ画像")
    application_requirements: Mapped[str] = mapped_column(sa.String(255), comment="募集要項")
    job_description: Mapped[str] = mapped_column(sa.String(255), comment="仕事内容")
    target_people: Mapped[str] = mapped_column(sa.String(255), comment="対象となる方")
    worklocation: Mapped[str] = mapped_column(sa.String(255), comment="勤務地")
    contract_period: Mapped[str] = mapped_column(sa.String(127), comment="契約期間")
    trial_period: Mapped[TrialPeriod] = mapped_column(IntEnum(TrialPeriod), comment="試用期間")
    salary_increment: Mapped[str] = mapped_column(sa.String(127), comment="昇給")
    bonus: Mapped[str] = mapped_column(sa.String(127), comment="賞与")
    overtime_work: Mapped[bool] = mapped_column(sa.Boolean(), comment="時間外勤務")
    overtime_work_free_input: Mapped[str] = mapped_column(sa.String(255), comment="時間外勤務の自由入力")
    holidays_or_vacation: Mapped[str] = mapped_column(sa.String(255), comment="休日・休暇")
    social_insurance: Mapped[str] = mapped_column(sa.String(127), comment="社会保険")
    welfare: Mapped[str] = mapped_column(sa.String(255), comment="福利厚生")
    training_system: Mapped[str] = mapped_column(sa.String(255), comment="研修制度")
    selection_method: Mapped[str] = mapped_column(sa.String(255), comment="選考方法")
    submitted_document: Mapped[str] = mapped_column(sa.String(255), comment="提出書類")
    employment_promotion_law: Mapped[str] = mapped_column(sa.String(255), comment="雇用推進法明示項目")
    contact_information: Mapped[str] = mapped_column(sa.String(255), comment="問い合わせ先")
    corporate_pr: Mapped[str] = mapped_column(sa.String(255), comment="企業PR")
    original_content1_title: Mapped[str] = mapped_column(sa.String(127), comment="オリジナルコンテンツ１のタイトル")
    original_content1_text: Mapped[str] = mapped_column(sa.Text(), comment="オリジナルコンテンツ１の本文")
    original_content2_title: Mapped[str] = mapped_column(sa.String(127), comment="オリジナルコンテンツ２のタイトル")
    original_content2_text: Mapped[str] = mapped_column(sa.Text(), comment="オリジナルコンテンツ２の本文")

    # relation
    company: Mapped["Company"] = relationship(back_populates="jobs")
    programming_languages: Mapped[list["ProgrammingLanguage"]] = relationship(back_populates="job")
    frameworks: Mapped[list["Framework"]] = relationship(back_populates="job")
    skills: Mapped[list["Skill"]] = relationship(back_populates="job")
    features: Mapped[list["Feature"]] = relationship(back_populates="job")
    areas: Mapped[list["Area"]] = relationship(back_populates="job")
    commuting_times: Mapped[list["CommutingTime"]] = relationship(back_populates="job")
    recruitment_flows: Mapped[list["RecruitmentFlow"]] = relationship(back_populates="job")
    recruitment_statuses: Mapped[list["RecruitmentStatus"]] = relationship(back_populates="job")
    occupational_ability_statuses: Mapped[list["OccupationalAbilityStatus"]] = relationship(back_populates="job")
    employment_management_statuses: Mapped[list["EmploymentManagementStatus"]] = relationship(back_populates="job")
    job_templates: Mapped[list["JobTemplate"]] = relationship(back_populates="job")
    reactions: Mapped[list["Reaction"]] = relationship(back_populates="job")
    selections: Mapped[list["Selection"]] = relationship(back_populates="job")
    favorite_jobs: Mapped[list["FavoriteJob"]] = relationship(back_populates="job")
