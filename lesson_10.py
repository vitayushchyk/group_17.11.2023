import decimal

INCHES = 2.7
MORTGAGE_YEAR_DURATION = 25
MORTGAGE_MONTH_DURATION = MORTGAGE_YEAR_DURATION * 12
INCOME_THRESHOLD_PERCENT = 0.35


def convert_cm_to_inches(cm: float) -> float:
    result = cm / INCHES
    return result


def get_even_numbers(income_list: list[int]) -> list[int]:
    result = [i for i in income_list if i % 2 == 0]
    return result


def check_mortgage(total: decimal, income: decimal) -> bool:
    mortgage_per_month = decimal.Decimal(total / MORTGAGE_MONTH_DURATION)
    income_threshold = decimal.Decimal(income * INCOME_THRESHOLD_PERCENT)
    result = mortgage_per_month < income_threshold
    return result
