# Working iwth Time duration, No. of words, WPM, Result acc. to marks

import json

# Load the JSON response from the AWS Transcribe output file
with open('jsonFiles/firstScript.json', 'r') as file:
    transcribe_output = json.load(file)

#end time
def endTime(transcribe_output):
    results = transcribe_output.get('results', {})
    if results:
        items = results.get('items', [])
        if items:
            end_times = [float(item.get('end_time', 0)) for item in items if 'end_time' in item]
            if end_times:
                end_time = max(end_times)  # Get the maximum end time
                #print("End Time Duration:", end_time)
                return end_time
            else:
                print("End time not found in any item.")
        else:
            print("No items found in the transcription output.")
    else:
        print("No results found in the transcription output.")

def wordCount(transcribe_output):
    word_count = transcribe_output.get('results', {}).get('transcripts', [{}])[0].get('transcript', '').count(' ') + 1
    return word_count



def WPM(word_count,end_time):
    wpm=word_count/(end_time/60)
    return wpm;

#average wpm by 1st grade student is : 60 wpm
avg_wpm=60

def reward(avg_wpm,wpm):
    if wpm>=avg_wpm:
        return "Good for Grade-1 student";
    elif wpm<=avg_wpm:
        return "need improvement";

et=endTime(transcribe_output);
wc=wordCount(transcribe_output);
wpm=int(WPM(wc, et));

print("Time duration of audio:",et)
print("Number of words:", wc)
print("Word per Minute:",wpm,"WPM")
print(reward(avg_wpm,wpm))