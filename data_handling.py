import json
from datetime import datetime

# Function to reformat the date
def reformat_date(date_str):
    # Convert the date from 'DD/MM/YYYY' to 'DD-MM-YYYY'
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    return date_obj.strftime("%d-%m-%Y")

# Read data from the input JSON file
with open('/home/srisha/ui/backend/dbms/abc.json', 'r') as infile:
    data = json.load(infile)

# Check if data is a list and update date_of_judgment for each item
if isinstance(data, list):
    for item in data:
        if "date_of_judgment" in item:
            item["date_of_judgment"] = reformat_date(item["date_of_judgment"])
else:
    print("Expected a list of items in the JSON file.")
    # If data is not a list, attempt to check if it's a single dictionary
    if isinstance(data, dict) and "date_of_judgment" in data:
        data["date_of_judgment"] = reformat_date(data["date_of_judgment"])

# Write the updated data to a new JSON file
with open('/home/srisha/ui/backend/dbms/final.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Date reformatted and new JSON file created: final.json")
