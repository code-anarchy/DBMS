import pdfplumber
import os

def check_judgment_formatting(file_path):
    """Check if the formatting (presence of 'JUDGMENT') is applicable in the file."""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if "JUDGMENT" in text.upper():  # Check if 'JUDGMENT' exists
                    return True  # The format is applicable
        return False  # 'JUDGMENT' was not found in the file
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def check_files_in_range(start=1, end=199):
    """Iterate through files named 1.pdf, 2.pdf,..., 199.pdf and check formatting."""
    applicable_files = []
    non_applicable_files = []

    for i in range(start, end + 1):
        file_name = f"{i}.pdf"
        if os.path.exists(file_name):  # Check if the file exists
            if check_judgment_formatting(file_name):
                applicable_files.append(file_name)
            else:
                non_applicable_files.append(file_name)
        else:
            print(f"{file_name} does not exist.")

    print("Files with applicable formatting (contain 'JUDGMENT'):")
    print(applicable_files)

    print("\nFiles without applicable formatting (do not contain 'JUDGMENT'):")
    print(non_applicable_files)

# Run the check for files from 1.pdf to 199.pdf
check_files_in_range(1, 1000)
