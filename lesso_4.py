from pprint import pprint

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

students['Платон Іванов'] = {
    'Пошта': 'Platon@gmail.com',
    'Вік': 26,
    'Номер телефону': None,
    'Середній бал': 98
}
students['Іван Петров']['bank_account_number'] = None
score_sum = 0
for student_info in students.values():
    score_sum += student_info['Середній бал']
average_score = score_sum / 4
salery_of_kurich = students['Женя Курич'].get('Зарплата', 0.0)

print(f'''
Середній бал групи : {average_score: .2f}
Зарплата Жені Курич : {salery_of_kurich}
''')
pprint(students)
