import json

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
    # Convert to lowercase and split into words
    return set(text.lower().split())

def find_missing_words(sample_words, transcribe_words):
    # Find words in sample words that are not in transcribed words
    return sample_words - transcribe_words

# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

# Read the content of the files
sample_text = read_text_file(text_file_path)
transcribe_text = read_transcribe_json(transcribe_json_path)

# Preprocess the text
sample_words = preprocess_text(sample_text)
transcribe_words = preprocess_text(transcribe_text)

# Find missing words
missing_words = find_missing_words(sample_words, transcribe_words)

print("Words missing from transcribed.json in sample.txt:", missing_words)

print("No. of Missing Words :",len(missing_words))


''' 
import json

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
    # Convert to lowercase and split into words
    return set(text.lower().split())

def find_missing_words(sample_words, transcribe_words):
    # Find words in sample words that are not in transcribed words
    return sample_words - transcribe_words

# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

# Read the content of the files
sample_text = read_text_file(text_file_path)
transcribe_text = read_transcribe_json(transcribe_json_path)

# Preprocess the text
sample_words = preprocess_text(sample_text)
transcribe_words = preprocess_text(transcribe_text)

# Find missing words
missing_words = find_missing_words(sample_words, transcribe_words)

print("Words missing from transcribed.json in sample.txt:", missing_words)
'''