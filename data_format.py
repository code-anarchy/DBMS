import os
import re
import json

# Directory containing the .txt files
input_directory = './'  # Adjust this if needed
output_directory = './filtered'  # New directory to store JSON files
os.makedirs(output_directory, exist_ok=True)

# Initialize a list to store all case data
all_cases_data = []

# Function to process each _data.txt file
def process_data_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Initialize the case dictionary
    case_data = {
        "petitioner": "",
        "respondent": "",
        "date_of_judgment": "",
        "bench": "",
        "citation": "",
        "citator_info": None,  # Set to None initially
        "judgment": ""  # Initialize judgment field
    }

    # Use regex to extract required fields
    petitioner_match = re.search(r'PETITIONER:\s*(.*?)\s*Vs\.', data, re.DOTALL)
    if petitioner_match:
        case_data['petitioner'] = petitioner_match.group(1).strip()

    respondent_match = re.search(r'RESPONDENT:\s*(.*?)\s*DATE OF JUDGMENT:', data, re.DOTALL)
    if respondent_match:
        case_data['respondent'] = respondent_match.group(1).strip()

    date_of_judgment_match = re.search(r'DATE OF JUDGMENT:\s*(.*?)\s*BENCH:', data)
    if date_of_judgment_match:
        case_data['date_of_judgment'] = date_of_judgment_match.group(1).strip()

    bench_match = re.search(r'BENCH:\s*(.*?)\s*BENCH:', data)
    if bench_match:
        # Extract first bench and remove duplicates and "BENCH:"
        benches = set(re.split(r',\s*', bench_match.group(1).strip()))
        case_data['bench'] = ', '.join(benches)

    citation_match = re.search(r'CITATION:\s*(.*?)\n', data)
    if citation_match:
        case_data['citation'] = citation_match.group(1).strip()
        
        # Check if there is a line for CITATOR INFO
        citator_info_match = re.search(r'CITATOR INFO :\s*(.*?)(?=\n\n|\Z)', data, re.DOTALL)
        if citator_info_match:
            case_data['citator_info'] = citator_info_match.group(1).strip()
        else:
            # If there's no citator info, assign the last line as citation
            last_line = data.strip().split('\n')[-1]
            case_data['citation'] = last_line.strip()

    return case_data

# Function to add judgment to each case
def add_judgment(case_data, judgment_file_path):
    if os.path.exists(judgment_file_path):
        with open(judgment_file_path, 'r', encoding='utf-8') as file:
            judgment_text = file.read().strip()
            case_data['judgment'] = judgment_text

# Iterate through each _data.txt file and process it
for i in range(1, 1000):
    data_file_name = f"{i}_data.txt"
    data_file_path = os.path.join(input_directory, data_file_name)

    if os.path.exists(data_file_path):
        case_data = process_data_file(data_file_path)

        # Now add the judgment from the corresponding *_judgement.txt file
        judgment_file_name = f"{i}_judgement.txt"
        judgment_file_path = os.path.join(input_directory, judgment_file_name)
        add_judgment(case_data, judgment_file_path)

        all_cases_data.append(case_data)

# Write all cases data to a single JSON file
output_file_path = os.path.join(output_directory, 'all_cases_data.json')
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_cases_data, json_file, ensure_ascii=False, indent=4)

print(f"Processed data written to {output_file_path}")
