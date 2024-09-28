import os


for i in range(199, 1001):
    os.system(f"wget --no-check-certificate main.sci.gov.in/jonew/judis/{i}.pdf")
    print(f"Downloaded {i}.pdf")