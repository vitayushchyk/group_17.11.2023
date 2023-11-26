string_cities = '6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$'
cities_list = string_cities.split()
for city in cities_list:
    clear_city = ''.join([letter for letter in city if letter.isalpha()])
    clear_city = clear_city.title()
    print(f'I \u2764️ {clear_city}')
