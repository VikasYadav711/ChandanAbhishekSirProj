'''
# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

'''
import json
import re
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
    # Remove specific symbols like "-", inverted commas, etc.
    text = re.sub(r'[^\w\s]', ' ', text)
    # Convert to lowercase
    return text.lower()

def get_unmatched_words(text1, text2):
    unmatched_words = []
    words1 = set(text1.split())
    words2 = set(text2.split())
    unmatched_words.extend(words1 - words2)
    unmatched_words.extend(words2 - words1)
    return unmatched_words

def calculate_similarity_ratio(text1, text2):
    return fuzz.ratio(text1, text2)

# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

# Read the content of the files
plain_text = read_text_file(text_file_path)
transcribe_text = read_transcribe_json(transcribe_json_path)

# Preprocess the text
plain_text = preprocess_text(plain_text)
transcribe_text = preprocess_text(transcribe_text)

# Get unmatched words
unmatched_words = get_unmatched_words(plain_text, transcribe_text)

print("Unmatched Words:", unmatched_words)



# Calculate similarity ratio
similarity_ratio = calculate_similarity_ratio(plain_text, transcribe_text)
print("Similarity Ratio:", similarity_ratio)

