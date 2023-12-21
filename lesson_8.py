import requests
import json

url_data = 'https://dummyjson.com/quotes?limit=100'
response = requests.get(url=url_data)
data = response.json()
with open('./data.json', mode='w') as file:
    json.dump(data, file, indent=4)
