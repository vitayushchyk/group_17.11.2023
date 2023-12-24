import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import config

mongo_url = config.MONGO_CONNECTION_STRING.format(
    user=config.MONGO_USER,
    password=config.MONGO_PASSWORD,
)
client = MongoClient(
    mongo_url,
    server_api=ServerApi('1'),
    tlsAllowInvalidCertificates=True
)
quotes_collection = client['quotesDB']['quotes']

raw_quotes = requests.get(config.QUOTES_SOURCE).json()
quotes_collection.insert_many(raw_quotes['quotes'])
result = quotes_collection.find({'author': "Albert Einstein"})
print(list(result))
result = quotes_collection.find({'quote': {'$regex': 'success'}})
print(list(result))
mark = quotes_collection.find({'author': "Mark Twain"})
query = {'author': "Mark Twain"}
operation = {'$set': {'favorite': True}}
updated = quotes_collection.update_many(query, operation)
print(updated)
result = quotes_collection.delete_many({'author': "Vincent Van Gogh"})
print(result)
result = quotes_collection.delete_many({})
print(result)
