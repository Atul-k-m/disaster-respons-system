from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['disaster_response']

def store_data(collection_name, data):
  collection = db[collection_name]
  if isinstance(data, list):
    for item in data:
      print(f"Inserting item: {item}")
      collection.insert_one(item)
  else:
    print(f"Inserting item: {data}")
    collection.insert_one(data)
