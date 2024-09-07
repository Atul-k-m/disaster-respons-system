from pymongo import MongoClient 
from bson import ObjectId
client = MongoClient('localhost', 27017)
db = client['disaster_response']

def store_data(collection_name, data):
    collection = db[collection_name]
    if isinstance(data, list):
        for item in data:
            if "_id" in item and isinstance(item["_id"], ObjectId):
                item["_id"] = str(item["_id"])  # Convert ObjectId to string
            print(f"Inserting item: {item}")
            collection.insert_one(item)
    else:
        if "_id" in data and isinstance(data["_id"], ObjectId):
            data["_id"] = str(data["_id"])  # Convert ObjectId to string
        print(f"Inserting item: {data}")
        collection.insert_one(data)