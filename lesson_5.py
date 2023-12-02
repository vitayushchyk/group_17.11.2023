import sys

import requests

url_carts = 'https://dummyjson.com/carts'

response = requests.get(url_carts)
if response.status_code != 200:
    print('''
x     x
   •
 _____
    ''')
    sys.exit(-1)
data_from_net = response.json()
carts = data_from_net['carts']

for cart in carts:
    if cart['userId'] == 56:
        for product in cart['products']:
            if product["discountPercentage"] > 15:
                print(product['title'])
