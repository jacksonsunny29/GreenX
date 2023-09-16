import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_key = os.getenv("OPENAIKEY")

# Define the list of keywords and the text to analyze
keywords = ["banana", "golf", "mountain", "giraffe", "elephant"]
text = "I want a banana. I don't want to play golf. I prefer giraffes to elephants."

prompt = (
    "i will provide a list of keywords. i will then provide a text. can you provide sentiment towards each keyword from the text.\n" +
    "keywords=" + str(keywords) + "\n" +
    "text=\"" + text + "\"\n" +
    "output the sentiment on a scale of -1 to 1. make the output a json serialised python dictionary with names enclosed in double quotes."
)

# Request sentiment analysis from GPT-3 in one API call
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100  # Adjust as needed
)

# Extract and structure the sentiment analysis for each keyword

# print(response)

sentiments = json.loads(response["choices"][0]["text"])

print(sentiments.values())