def convert_cm_to_inches(cm):
    return cm / 2.7


def get_even_numbers(income_list: list[int]) -> list[int]:
    return [i for i in income_list if i % 2 == 0]


def check_mortgage(total, income) -> bool:
    return (total / 25 / 12) < (income * 0.35)
