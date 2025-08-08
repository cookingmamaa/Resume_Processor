##----------------------------------------------------------------
## Title: main.py
## Purpose: Extract relevant information from PDF resume files for processing
## Notes: 
## Author: AA
##----------------------------------------------------------------

##----------------------------------------------------------------
## 0. Environment setup
##----------------------------------------------------------------
import os
import pdfplumber
import spacy
import re
import pandas as pd

##----------------------------------------------------------------
## 1. Create list of files from Data directory
##----------------------------------------------------------------
# Path to your directory
fp_data = r"C:/Users/aches/Desktop/Stuff/Coding/Resume_Processor_Data/"

# Create a list of all files in the directory
file_list = []

# Loop through directory
for filename in os.listdir(fp_data):
    file_path = os.path.join(fp_data, filename)
    file_list.append(file_path)

# Print the list of files
print(file_list)

##----------------------------------------------------------------
## 2. Scrape text with pdfplumber
##----------------------------------------------------------------
parsed_text_list = {}

for file in file_list:
    parsed_text = ""
    filename = os.path.basename(file)
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            parsed_text += page.extract_text() + "\n"
    parsed_text_list[filename] = parsed_text

print(parsed_text)
parsed_text_list.keys()
print(parsed_text_list['Alistair Acheson - Resume (DE).pdf'])
print(parsed_text_list['Resume-Sample-1-Software-Engineer.pdf'])

##----------------------------------------------------------------
## 3. Create table & Extract relevant information from resume
##----------------------------------------------------------------

# Create pd.Dataframe to store data
df = pd.DataFrame(columns=[
    "filename",
    "extracted_text",
    
    "Name",
    "Email",
    "Phone",
    "Skills",
    "Education",
    "Experience"
])


# How to print an indexed value from the resumes
list(parsed_text_list.values())[1]

# Extract email
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
matches = re.findall(email_pattern, list(parsed_text_list.values())[1])


##----------------------------------------------------------------
## 3. Use spaCy to detect relevant information from resume text
##----------------------------------------------------------------

# load model
nlp = spacy.load("en_core_web_sm")

# process text
doc = nlp(list(parsed_text_list.values())[1])

# Named Entity Recognition
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

# Tokenization example
for token in doc:
    print(token.text, token.pos_, token.dep_)
