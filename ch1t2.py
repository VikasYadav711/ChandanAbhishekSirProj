import json
from fuzzywuzzy import fuzz

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_transcribe_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Extract text from the JSON file obtained from AWS Transcribe
    transcribe_text = ""
    for item in data["results"]["items"]:
        if item["type"] == "pronunciation":
            transcribe_text += item["alternatives"][0]["content"] + " "
    return transcribe_text.strip()

def preprocess_text(text):
    # Add preprocessing steps here if needed
    return text.lower()

def compare_text_files(text1, text2):
    # Preprocess the text
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Compare the text using FuzzyWuzzy
    similarity_score = fuzz.ratio(text1, text2)
    
    return similarity_score

# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

# Read the content of the files
plain_text = read_text_file(text_file_path)
transcribe_text = read_transcribe_json(transcribe_json_path)

# Compare the text files
similarity_score = compare_text_files(plain_text, transcribe_text)
print("Similarity Score:", similarity_score)
