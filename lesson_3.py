string_cities = '6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$'
cities_list = string_cities.split()
for city in cities_list:
    clear_city = ''.join([letter for letter in city if letter.isalpha()])
    clear_city = clear_city.title()
    print(f'I \u2764️ {clear_city}')

# string_cities = '6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$'
# new_list = string_cities.replace('6..58', '').replace('74$:?$', '').title().split()
# for city in new_list:
#     print(f'I \u2764️ {city}')
