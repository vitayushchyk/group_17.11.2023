import decimal

RETIREMENT_AGE = 65
STRING_HEADER = ' ~' * 40
USD_EXCHANGE_RATE = decimal.Decimal('37.3')
CAR_PRICE = 31500

user_name = input('What is your name?\n')
user_name = user_name.strip().title()

user_age = int(input('What is your age?\n'))

salary_month = decimal.Decimal(input('What is your monthly salary?\n'))

years_until_retirement = RETIREMENT_AGE - user_age

career_money_earned = years_until_retirement * 12 * salary_month

conversion_dollars = career_money_earned / USD_EXCHANGE_RATE

count_toyota = conversion_dollars // CAR_PRICE

print(f'''
{STRING_HEADER}
I'm, {user_name}, will only be able to earn {conversion_dollars:.2f} dollars,
which is enough for only {count_toyota} Toyotas,
I'm not satisfied with this, so I will change my life and study programming hard!
''')
