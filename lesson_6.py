import requests

url_data = 'https://script.google.com/macros/s/AKfycbwlDeTALkaaQ6Kb51eSXf_51bg-vK89TfIUJJ_EUMExcf7VKuCaS-HbMDZ-go08odU4/exec'
response = requests.get(url=url_data)
data_from_google_table = response.json()
number_of_big_family = 0
monthly_income_of_people = 0
quantity_family_with_big_credit = 0
women_with_their_own_house = 0
for data in data_from_google_table['data']:
    if data['age'] >= 35 and data['large family']:
        monthly_income_of_people += data['monthly income, $']

    if data['large family']:
        number_of_big_family += 1

    if data['credit'] >= data['monthly income, $']:
        quantity_family_with_big_credit += 1

    if data['gender'] == 'male' and data['own home']:
        women_with_their_own_house += 1

print(f'''
Monthly income of people whose family is large and whose age is more than 35 years = {monthly_income_of_people}
The number of large families = {number_of_big_family}
The quantity of families in which loan expenses are greater than income = {quantity_family_with_big_credit}
Number of women who own their own home = {women_with_their_own_house}
''')
