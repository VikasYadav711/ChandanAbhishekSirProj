'''
# Example usage
text_file_path = 'chapter1.txt'
transcribe_json_path = 'Ch1transcript.json'

'''
import json
import re
from fuzzywuzzy import fuzz
from datetime import datetime

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

#Similarity Ratio Function
def calculate_similarity_ratio(text1, text2):
    return fuzz.ratio(text1, text2)

#Similarity Ratio using PSM
def calculate_SR_PSM(text1,text2):
    return fuzz.partial_ratio(text1,text2)

#Similarity 

def get_word_count(text):
    # Count the number of words in the text
    return len(text.split())



def read_transcribe_json2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def calculate_audio_duration2(transcribe_data):
    # Extract timestamps from the JSON file obtained from AWS Transcribe
    timestamps = []
    for item in transcribe_data["results"]["items"]:
        if item["type"] == "pronunciation":
            timestamps.append(float(item["start_time"]))

    # Calculate total duration
    total_duration = max(timestamps) - min(timestamps)
    return total_duration/60  # convert to minutes


#WPM
def wpm(total_duration, word_count_transcribe_text):
    return word_count_plain_text/total_duration



'''

#Preprocess for missing words
def preprocess_text2(text):
    # Convert to lowercase and split into words
    return set(text.lower().split())

#Missing Words
def find_missing_words(text1, text2):
    # Find words in text2 that are not in text1
    return text2 - text1
'''


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
print("")


# Calculate similarity ratio
similarity_ratio = calculate_similarity_ratio(plain_text, transcribe_text)
print("Similarity Ratio:", similarity_ratio)


#PSR=partial string matching
similarity_ratio_PSM= calculate_SR_PSM(plain_text,transcribe_text)
print("Similarity Ratio after doing PSR, in % :",similarity_ratio_PSM)


# Get word count for both texts
word_count_plain_text = get_word_count(plain_text)
word_count_transcribe_text = get_word_count(transcribe_text)

print("No. of Words in Source File: ", word_count_plain_text)
print("No. of words in transcibed File: ", word_count_transcribe_text)



# Example usage for time duration

# Read the content of the JSON file
transcribe_data2 = read_transcribe_json2(transcribe_json_path)

# Calculate total audio duration
total_duration = calculate_audio_duration2(transcribe_data2)
formatted_time="{:.{}f}".format(total_duration,2)
print("Total Audio Duration (minutes):", formatted_time,"min")


#WPM
formatted_wpm = "{:.{}f}".format(wpm(total_duration, word_count_transcribe_text), 2)
print("Words Per Minute :",formatted_wpm, "WPM")





'''
# Read the content of the files
plain_text3 = read_text_file(text_file_path)
transcribe_text3 = read_transcribe_json(transcribe_json_path)

# Preprocess the text
plain_words3 = preprocess_text2(plain_text3)
transcribe_words3 = preprocess_text2(transcribe_text3)

# Find missing words
missing_words = find_missing_words(plain_text3,transcribe_text3)

print("Words missing from sample.txt in transcribed.json:", missing_words)
'''