from app.choices.base import BaseIntEnum


class SalarySystem(BaseIntEnum):
    """
    給与形態
    """

    ANNUAL_INCOME = 1, "年収"
    MONTHLY_SALARY = 2, "月給"
    HOURLY_WAGE = 3, "時給"
