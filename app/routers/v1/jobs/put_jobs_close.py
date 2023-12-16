from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.jobs.job_response import JobResponse

router = APIRouter()


@router.put(
    "/{job_id}/close",
    response_model=JobResponse,
    summary="スカウト求人掲載",
)
async def put_jobs_close(
    job_id: int = Path(..., ge=1, description="求人ID"),
    session: AsyncSession = Depends(get_session),
) -> JobResponse:
    """スカウト求人を掲載する"""

    if job_id is None:
        # TODO: エラー処理
        pass

    return {
        "job_id": 1,
        "job_title": "string",
        "skill_level": 0,
        "job_image": "",
        "salary_form": 1,
        "min_salary_amount": 10,
        "max_salary_amount": 100,
        "areas": [{"area_id": 1, "area_name": "string"}],
        "features": [{"feature_id": 1, "feature_name": "string"}],
        "programming_languages": [{"programming_language_id": 1, "programming_language_name": "string"}],
        "frameworks": [{"framework_id": 1, "framework_name": "string"}],
        "skills": [{"skill_id": 1, "skill_name": "string"}],
        "update_at": "2019-08-24",
        "publication_start_date": "2019-08-24",
        "publication_end_date": "2019-08-24",
        "occupation": {"occupation_id": 1, "occupation_name": "string"},
        "job_description": "string",
        "target_people": "string",
        "work_location": "string",
        "number_of_people_hired": 10,
        "initiatives_to_prevent_passive_smoking": 1,
        "employment_status": 1,
        "contract_period": "string",
        "trial_period": 0,
        "salary_supplement": "string",
        "salary_increment": "string",
        "bonus": "string",
        "commuting_time": [{"commuting_time_from": "10:00:00", "commuting_time_to": "12:00:00"}],
        "commuting_time_supplement": "string",
        "overtime_work": True,
        "overtime_work_free_input": "string",
        "holidays_or_vacation": "string",
        "social_insurance": "string",
        "welfare": "string",
        "training_system": "string",
        "recruitment_flows": ["string"],
        "selection_method": "string",
        "submitted_document": "string",
        "recruitment": [{"recruitment_status": 1, "recruitment_status_free_input": "string"}],
        "occupational_ability": [{"occupational_ability_status": 1, "occupational_ability_status_free_input": "string"}],
        "employment_management": [{"employment_management_status": 1, "employment_management_status_free_input": "string"}],
        "contact_information": "string",
        "corporate_pr": "string",
        "original_content1_title": "string",
        "original_content1_text": "string",
        "original_content2_title": "string",
        "original_content2_text": "string",
    }
