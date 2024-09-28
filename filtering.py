import os
import re

# Paths
input_folder_path = "cases"  # Replace with the path to your folder containing the .txt files
output_folder_path = os.path.join(input_folder_path, "filtered")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Regular expression to match unwanted lines like "http://JUDIS.NIC.IN SUPREME COURT OF INDIA Page X of Y"
unwanted_line_pattern = re.compile(r"http://JUDIS\.NIC\.IN SUPREME COURT OF INDIA Page \d+ of \d+")

# Function to clean unwanted lines
def clean_text(text):
    return "\n".join([line for line in text.splitlines() if not unwanted_line_pattern.match(line)])

# Function to split file content
def split_case_file(file_content):
    # Split text at the first occurrence of "ACT:"
    split_text = file_content.split("ACT:", 1)
    
    # If "ACT:" is found, return the two parts
    if len(split_text) == 2:
        data_part = split_text[0]
        judgement_part = "ACT:" + split_text[1]  # Keep the "ACT:" part in the second file
        return clean_text(data_part), clean_text(judgement_part)
    else:
        # If no "ACT:" found, return the entire text as the first part
        return clean_text(file_content), None

# Process each file in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        # Split the content into data and judgement parts
        data_part, judgement_part = split_case_file(file_content)
        
        # Get the base name like '1', '2', etc.
        base_name = os.path.splitext(filename)[0]
        
        # Save the processed files in the filtered directory
        data_filename = os.path.join(output_folder_path, f"{base_name}_data.txt")
        judgement_filename = os.path.join(output_folder_path, f"{base_name}_judgement.txt")
        
        # Save the data part
        with open(data_filename, 'w', encoding='utf-8') as data_file:
            data_file.write(data_part)
        
        # Save the judgement part, if available
        if judgement_part:
            with open(judgement_filename, 'w', encoding='utf-8') as judgement_file:
                judgement_file.write(judgement_part)
        
        print(f"Processed {filename} into {data_filename} and {judgement_filename}")

print(f"All files processed successfully and saved in '{output_folder_path}'.")
