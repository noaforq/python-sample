from fastapi import APIRouter, Depends, Query

from app.db import AsyncSession, get_session
from app.schemas.masters.masters_response import MasterResponse

router = APIRouter()


@router.get(
    "",
    response_model=MasterResponse,
    summary="マスターデータを取得する",
    # responses=error_response(ValidationError),
)
async def get_masters(
    is_get_occupations: bool = Query(False, description="職種データ取得するかどうか"),
    is_get_programming_languages: bool = Query(False, description="プログラミング言語を取得するかどうか"),
    is_get_frameworks: bool = Query(False, description="フレームワークデータを取得するかどうか"),
    is_get_skills: bool = Query(False, description="スキルデータを取得するかどうか"),
    is_get_features: bool = Query(False, description="特徴データを取得するかどうか"),
    is_get_areas: bool = Query(False, description="エリアデータを取得するかどうか"),
    is_get_industries: bool = Query(False, description="業種データを取得するかどうか"),
    is_get_schools: bool = Query(False, description="学校データを取得するかどうか"),
    is_get_faculty: bool = Query(False, description="学部データを取得するかどうか"),
    is_get_qualification: bool = Query(False, description="資格データを取得するかどうか"),
    is_get_programming_experience: bool = Query(False, description="プログラミング経験データを取得するかどうか"),
    session: AsyncSession = Depends(get_session),
) -> dict:
    """マスターデータを取得する"""
    # ロジック部分は後ほど記述
    result = MasterResponse()

    # TODO: serviceクラスに後ほどメソッド切り出し
    if is_get_occupations:
        occupations = [
            {"occupation_id": 1, "occupation_name": "string"},
            {"occupation_id": 2, "occupation_name": "string2"},
            {"occupation_id": 3, "occupation_name": "string3"},
        ]
        result.occupations = occupations

    if is_get_programming_languages:
        programming_languages = [
            {"programming_language_id": 1, "programming_language_name": "string"},
            {"programming_language_id": 2, "programming_language_name": "string2"},
            {"programming_language_id": 3, "programming_language_name": "string3"},
        ]
        result.programming_languages = programming_languages

    if is_get_frameworks:
        frameworks = [
            {"framework_id": 1, "framework_name": "string"},
            {"framework_id": 2, "framework_name": "string2"},
            {"framework_id": 3, "framework_name": "string3"},
        ]
        result.frameworks = frameworks

    if is_get_skills:
        skills = [
            {"skill_id": 1, "skill_name": "string"},
            {"skill_id": 2, "skill_name": "string2"},
            {"skill_id": 3, "skill_name": "string3"},
        ]
        result.skills = skills

    if is_get_features:
        features = [
            {"feature_id": 1, "feature_name": "string"},
            {"feature_id": 2, "feature_name": "string2"},
            {"feature_id": 3, "feature_name": "string3"},
        ]
        result.features = features

    if is_get_areas:
        areas = [
            {"area_id": 1, "area_name": "string"},
            {"area_id": 2, "area_name": "string2"},
            {"area_id": 3, "area_name": "string3"},
        ]
        result.areas = areas

    if is_get_industries:
        industries = [
            {"industry_id": 1, "industry_name": "string"},
            {"industry_id": 2, "industry_name": "string2"},
            {"industry_id": 3, "industry_name": "string3"},
        ]
        result.industries = industries

    if is_get_schools:
        schools = [
            {"school_id": 1, "school_name": "string"},
            {"school_id": 2, "school_name": "string2"},
            {"school_id": 3, "school_name": "string3"},
        ]
        result.schools = schools

    if is_get_faculty:
        faculties = [
            {"faculty_id": 1, "faculty_name": "string"},
            {"faculty_id": 2, "faculty_name": "string2"},
            {"faculty_id": 3, "faculty_name": "string3"},
        ]
        result.faculties = faculties

    if is_get_qualification:
        qualification = [
            {"qualification_id": 1, "qualification_name": "string"},
            {"qualification_id": 2, "qualification_name": "string2"},
            {"qualification_id": 3, "qualification_name": "string3"},
        ]
        result.qualification = qualification

    if is_get_programming_experience:
        programming_experience = [
            {"programming_experience_id": 1, "programming_experience_name": "string"},
            {"programming_experience_id": 2, "programming_experience_name": "string2"},
            {"programming_experience_id": 3, "programming_experience_name": "string3"},
        ]
        result.programming_experience = programming_experience

    return result
