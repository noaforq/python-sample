from pydantic import Field

from app.schemas.base import PydanticModel


class SelectionsManageResponseSelection(PydanticModel):
    job_id: str = Field(..., description="求人ID")
    job_title: str = Field(..., description="求人タイトル")
    student_id: str = Field(..., description="応募している学生（以下学生）アカウントのID")
    student_fullname: str = Field(..., description="学生の本名")
    student_address: str = Field(..., description="学生の居住地（現状都道府県まで）")
    student_age: int = Field(..., description="学生の年齢")
    student_preferred_programming_languages: list[str] = Field(..., description="得意な言語")
    student_preferred_frameworks: list[str] = Field(..., description="得意なフレームワーク")
    employment_status: int = Field(
        ...,
        description="雇用形態。1 FULL_TIME、2 INTERN、3 PART_TIMER、4 NEW_GRADUATE、5 CONTRACT_EMPLOYEE、6 SUBCONTRACTING、7 TEMPORARY_EMPLOYEE",
    )
    selection_step: int = Field(
        ...,
        description="選考状況。10 応募中、11 スカウト承認待ち、20 書類選考、21 1次面接、22 2次面接、23 3次面接、24 4次面接、25 5次面接、30 内定出し、31 内定承諾、32 入社済み、40 スカウト不承諾、41 お見送り、42 辞退、49 終了",
    )
    selection_method: int = Field(..., description="求人の選考ルート。1 スカウト、2 応募")
    message_timeline_id: str = Field(..., description="メッセージタイムラインID")
    start_date: str = Field(..., description="選考開始予定日")
    end_date: str = Field(..., description="選考終了予定日")
    update_date: str = Field(..., description="")
    entry_date: str = Field(..., description="選考開始日")
    last_message_date: str = Field(..., description="最後にメッセージをやり取りした日")
    memo: str = Field(..., description="選考に紐づくメモ")


class SelectionsManageResponse(PydanticModel):
    total_page: int = Field(..., description="総ページ数")
    current_page: int = Field(..., description="現在のページ")
    selections: list[SelectionsManageResponseSelection] = Field(..., description="選考一覧")
