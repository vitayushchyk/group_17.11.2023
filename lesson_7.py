import csv

with open('./airport-codes_csv.csv') as csvfile:
    airports = csv.DictReader(csvfile, delimiter=';')
    for row in airports:
        if row['iso_country'] == 'UA':
            print(row['name'])
