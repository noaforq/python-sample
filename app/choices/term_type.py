from app.choices.base import BaseIntEnum


class TermType(BaseIntEnum):
    """
    規約種別
    """

    GENERAL_TERM_OF_USE = 1, "利用規約 (一般ユーザー)"
    GENERAL_PRIVACY_POLICY = 2, "プライバシーポリシー (一般ユーザー）"
    GENERAL_NEW_REGISTRATION = 3, "新規登録時の注意事項 (一般ユーザー)"
    HR_PERSONAL_ID_INFO_TERM = 4, "人材紹介 個人情報規約"
    HR_TERM_OF_USE = 5, "人材紹介 利用規約"
    SCHOOL_TERM_OF_USE = 6, "学校 利用規約"
    COMPANY_TERM_OF_USE = 7, "企業 利用規約"
