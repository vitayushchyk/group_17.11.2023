def get_cities(prompt: str) -> set[str]:
    raw_response = input(prompt)
    result = set(raw_response.strip().title().split(' '))
    return result


visited_cities = get_cities('Вкажіть міста, в котрих ви були: ')
citi_plan = get_cities('Вкажіть міста, котрі, ви хочете відвідати: ')
loved_cities = citi_plan.intersection(visited_cities)
new_cities = citi_plan.difference(visited_cities)
print(f"""Вам, напевно, дуже сподобалось в містах {' '.join(loved_cities)}
Ви відкритий до чогось нового {' '.join(new_cities)}
""")
