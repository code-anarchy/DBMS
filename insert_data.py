import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
# Assuming you have already set up your MongoDB connection
uri = "mongodb+srv://codesrisha:Zygf4fUYScWteOWk@cluster0.my38l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["abdsa"] 

def insert_data(collection_name: str, data: dict):
    collection = db[collection_name]
    try:
        result = collection.insert_one(data)
        print(f"Data inserted with id: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting data: {e}")

def upload_json_to_mongodb(file_path: str, collection_name: str):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data from the file

        # If the data is a list, iterate through each item
        if isinstance(data, list):
            for item in data:
                insert_data(collection_name, item)
        else:
            insert_data(collection_name, data)  # If it's a single dictionary

# Usage
upload_json_to_mongodb('/home/srisha/ui/backend/dbms/updated-abcabc.json', 'casess')
