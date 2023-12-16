from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsResponseEmploymentManagement(PydanticModel):
    employment_management_status: int = Field(..., description="企業における雇用管理に関する状況。1 PAID_HOLIDAY、2 CHILDCARE_LEAVE、3 PERCENTAGE_OF_WOMEN")
    employment_management_status_free_input: str = Field(..., description="企業における雇用管理に関する状況詳細")


class SelectionsResponseOccupationalAbility(PydanticModel):
    occupational_ability_status: int = Field(..., description="職業能力の開発・向上に関する状況。1 TRAINING、2 SELF_ENLIGHTENMENT、3 MENTOR、4 CAREER_CONSULTING、5 IN_HOUSE_TEST")
    occupational_ability_status_free_input: str = Field(None, description="企業における雇用管理に関する状況詳細")


class SelectionsResponseRecruitment(PydanticModel):
    recruitment_status: int = Field(
        ...,
        description="募集採用に関する状況。1 NUM_OF_HIRES_AND_JOB_LEAVERS、2 NUM_OF_HIRES_BY_GENDER、3 AVERAGE_LENGTH_OF_SERVICE",
    )
    recruitment_status_free_input: str = Field(None, description="募集採用に関する状況詳細")


class SelectionsResponseCommutingTime(PydanticModel):
    commuting_time_from: str = Field(..., description="始業時間")
    commuting_time_to: str = Field(..., description="終業時間")


class SelectionsResponseOccupation(PydanticModel):
    m_occupation_id: int = Field(..., description="始業時間")
    commuting_time_to: str = Field(..., description="終業時間")


class SelectionsResponseSkill(PydanticModel):
    skills_id: int = Field(..., description="スキルID")
    skills_name: str = Field(..., description="スキル名")


class SelectionsResponseFramework(PydanticModel):
    frameworks_id: int = Field(..., description="フレームワークID")
    frameworks_name: str = Field(..., description="フレームワーク名")


class SelectionsResponseProgrammingLanguage(PydanticModel):
    programming_languages_id: int = Field(..., description="フレームワークID")
    programming_languages_name: str = Field(..., description="フレームワーク名")


class SelectionsResponseFeature(PydanticModel):
    features_id: int = Field(..., description="フレームワークID")
    features_name: str = Field(..., description="フレームワーク名")


class SelectionsResponseArea(PydanticModel):
    area_id: int = Field(..., description="エリアID")
    area_name: str = Field(..., description="エリア名")


class SelectionsResponseJob(PydanticModel):
    job_title: str = Field(..., description="求人ポジション名")
    skill_level: int | None = Field(None, description="スキルレベル。0 CLASSLESS、1 BEGINNER、2 ELEMENTARY、3 INTERMEDIATE、4 ADVANCED")
    job_image: str = Field(None, description="求人画像")
    salary_from: int = Field(None, description="給与形態。1 ANNUAL_INCOME、2 MONTHLY_SALARY、3 HOURLY_WAGE")
    min_salary_amount: int = Field(None, description="最小給与額")
    max_salary_amount: int = Field(None, description="	最大給与額")
    area: list[SelectionsResponseArea] = Field(None, description="エリア")
    features: list[SelectionsResponseFeature] = Field(None, description="特徴")
    programming_languages: list[SelectionsResponseProgrammingLanguage] = Field(None, description="プログラミング言語")
    frameworks: list[SelectionsResponseFramework] = Field(None, description="フレームワーク")
    skills: list[SelectionsResponseSkill] = Field(None, description="スキル")
    update_at: str = Field(..., description="最終更新日")
    publication_start_date: str = Field(..., description="掲載開始日")
    publication_end_date: str = Field(..., description="掲載終了日")
    occupation: list[SelectionsResponseOccupation] = Field(None, description="職種")
    job_description: str = Field(..., description="仕事内容")
    target_people: str | None = Field(..., description="対象となる方")
    work_location: str = Field(..., description="勤務地")
    number_of_people_hired: int = Field(None, description="採用人数")
    initiatives_to_prevent_passive_smoking: int = Field(
        ...,
        description="集合場所における受動喫煙防止の取り組み。1 NOTHING、2 NO_SMOKING_ON_SITE、3 NO_SMOKING_INDOORS、4 NO_SMOKING_INDOORS_PRINCIPLE、5 INDOOR_SMOKING_ALLOWED、6 OUTDOOR_SMOKING_ALLOWED、7 OTHERS",
    )
    employment_status: int = Field(
        ...,
        description="雇用形態。1 FULL_TIME、2 INTERN、3 PART_TIMER、4 NEW_GRADUATE、5 CONTRACT_EMPLOYEE、6 SUBCONTRACTING、7 TEMPORARY_EMPLOYEE",
    )
    contract_period: str = Field(..., description="雇用期間")
    trial_period: int = Field(..., description="試用期間。0 NOTHING、1 ONE_MONTH、2 TWO_MONTH、3 THREE_MONTH、4 FOUR_MONTH、5 FIVE_MONTH、6 SIX_MONTH")
    salary_supplement: str = Field(None, description="給与補足")
    salary_increment: str = Field(None, description="昇給")
    bonus: str = Field(None, description="賞与")
    commuting_time: list[SelectionsResponseCommutingTime] = Field(None, description="勤務時間")
    commuting_time_supplement: str = Field(None, description="勤務時間補足")
    overtime_work: bool = Field(None, description="時間外勤務")
    overtime_work_free_input: str = Field(None, description="時間外勤務の自由入力")
    holidays_or_vacation: str = Field(None, description="休日・休暇")
    welfare: str = Field(..., description="福利厚生")
    training_system: str = Field(None, description="研修制度")
    recruitment_flows: list[str] = Field(None, description="福利厚生")
    selection_method: str = Field(None, description="選考方法")
    submitted_document: str = Field(None, description="提出書類")
    recruitment: list[SelectionsResponseRecruitment] = Field([], description="募集採用に関する状況に関して")
    occupational_ability: list[SelectionsResponseOccupationalAbility] = Field([], description="職業能力の開発・向上に関する状況に関して")
    employment_management: list[SelectionsResponseEmploymentManagement] = Field([], description="企業における雇用管理に関して")
    contact_information: str = Field(None, description="問い合わせ先")
    original_content1_title: str = Field(None, description="オリジナルコンテンツ1タイトル")
    original_content1_text: str = Field(None, description="オリジナルコンテンツ1本文")
    original_content2_title: str = Field(None, description="オリジナルコンテンツ2タイトル")
    original_content2_text: str = Field(None, description="オリジナルコンテンツ2本文")
    company_name: str = Field(..., description="企業名")
    formal_name: str = Field(..., description="企業の正式名")
    logo_image_uri: str = Field(..., description="企業ロゴのURI")
    image_uri: str = Field(..., description="企業のサムネイルURI")
    corporate_website_uri: str = Field(..., description="コーポレートサイトURI")
    contact_email_address: str = Field(..., description="連絡先メールアドレス")
    address: str = Field(..., description="企業所在地")
    number_of_employee: int = Field(..., description="従業員数")
    average_age: int = Field(..., description="平均年齢")
    establishment_date: int = Field(..., description="	設立日")
    capital_stock: int = Field(..., description="資本金")
    major_shareholder: str = Field(..., description="主要株主")
    sales: int = Field(..., description="売上")
    recruitment_record: str = Field(..., description="主要株主")
    description: str = Field(..., description="主要株主")
    business_detail: str = Field(..., description="主要株主")
    philosophy: str = Field(..., description="主要株主")
    chief_executive_officer: str = Field(..., description="主要株主")


class SelectionsResponseSelection(PydanticModel):
    message_timeline_id: str = Field(..., description="メッセージタイムラインのID")
    job: SelectionsResponseJob = Field(..., description="none")
    selection_method: str | None = Field(..., description="選考ルート")
    selection_step: int = Field(
        ...,
        ge=0,
        description="選考状況。10 応募中、11 スカウト承認待ち、20 書類選考、21 1次面接、22 2次面接、23 3次面接、24 4次面接、25 5次面接、30 内定出し、31 内定承諾、32 入社済み、40 スカウト不承諾、41 お見送り、42 辞退、49 終了",
    )
    start_date: str = Field(..., description="選考開始予定日")
    end_date: str = Field(..., description="選考終了予定日")
    memo: str = Field(..., description="選考に紐づくメモ")
    update_date: str = Field(..., description="")
    entry_date: str = Field(..., description="選考開始日")
    last_message_date: str = Field(..., description="最後にメッセージをやり取りした日")
    has_added_in_favorites: bool = Field(False, description="お気に入りに登録済みか。true 登録済み、false 登録していない")


class SelectionsResponse(PydanticModel):
    total_page: int = Field(..., description="総ページ数")
    current_page: int = Field(..., description="現在のページ")
    selections: list[SelectionsResponseSelection] = Field(..., description="選考一覧")
