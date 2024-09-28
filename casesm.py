import pdfplumber
import os

# Create a function to extract text from PDFs and save to corresponding text files
def extract_pdf_to_text(start=1, end=999):
    for i in range(start, end + 1):
        pdf_filename = f"cases/{i}.pdf"
        txt_filename = f"cases/{i}.txt"

        # Check if the PDF file exists
        if True:
            with pdfplumber.open(pdf_filename) as pdf:
                full_text = ""
                for page in pdf.pages:
                    full_text += page.extract_text() + "\n"

            # Write the extracted text to a .txt file
            with open(txt_filename, 'w', encoding='utf-8') as txt_file:
                txt_file.write(full_text)

            print(f"Extracted text from {pdf_filename} to {txt_filename}")
        else:
            print(f"{pdf_filename} not found.")

# Run the extraction for PDFs 1 to 999
extract_pdf_to_text(1, 999)
