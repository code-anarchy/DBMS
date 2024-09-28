import pymongo
from pymongo.errors import ConnectionFailure, OperationFailure, ConfigurationError

def fetch_data_from_mongodb(mongodb_uri, database_name, collection_name):
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(mongodb_uri)
        
        # Check if the connection was successful
        client.admin.command('ismaster')
        
        # Select the database and collection
        db = client[database_name]
        collection = db[collection_name]
        
        # Fetch all documents from the collection
        data = list(collection.find())
        
        print(f"Successfully fetched {len(data)} documents from MongoDB")
        return data
    
    except ConnectionFailure:
        print("Error: Could not connect to MongoDB")
    except ConfigurationError as e:
        print(f"Error: MongoDB configuration error - {str(e)}")
    except OperationFailure as e:
        print(f"Error: MongoDB operation failed - {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

# MongoDB connection details
uri = "mongodb+srv://swatantratiwari29:Niggaballz@adaalat.1q8sc.mongodb.net/?retryWrites=true&w=majority&appName=Adaalat"
database_name = "legal_cases_db"
collection_name = "cases"

# Fetch data from MongoDB
fetched_data = fetch_data_from_mongodb(uri, database_name, collection_name)

# You can now use 'fetched_data' for further processing
if fetched_data:
    print("Data fetched successfully. Ready for further processing.")
else:
    print("Failed to fetch data from MongoDB.")

# if fetched_data and len(fetched_data) > 1:
#     print(fetched_data[1].get('summary', 'Summary not found'))
# else:
#     print("Not enough data to access the second document's summary.")


# reqid = input("Enter the case number: ")


# # print(fetched_data[0].get('case_number'))

# case_found = False
# for i in fetched_data:
#     if i.get('case_number') == reqid:
#         print(i.get('summary'))
#         case_found = True
#         break

# if not case_found:
#     print("Case not found")


# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def members():
    data = {"message": "Hello from the backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)