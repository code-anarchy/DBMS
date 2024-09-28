import pdfplumber

def extract_judgment_lines(file_path):
    with pdfplumber.open(file_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()

    # Split text into lines
    lines = full_text.split('\n')

    # Identify the start and end of the judgment part
    judgment_start = False
    judgment_lines = []

    for line in lines:
        # Detect where the judgment begins
        if "JUDGMENT" in line.upper():
            judgment_start = True
        if judgment_start:
            # Skip unnecessary page markers or irrelevant details
            if line.strip().startswith("http"):
                continue
            # Append relevant lines for the judgment
            judgment_lines.append(line)

    # Join judgment lines into a single string (preserving the original formatting)
    cleaned_judgment = "\n".join(judgment_lines)

    return cleaned_judgment


# Usage example
for i in range(1,200):
    file_path = f"{i}.pdf"
    judgment_text = extract_judgment_lines(file_path)

    # Save the cleaned judgment to a file or print it out
    with open(f"extracted_judgment_{i}.txt", "w") as f:
        f.write(judgment_text)

print("Judgment extraction complete with line formatting preserved.")
