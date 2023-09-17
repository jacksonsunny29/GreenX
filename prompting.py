import os
from pyexpat.errors import messages
import openai
from dotenv import load_dotenv
import json

load_dotenv()

class TextAnalyser(object):

    openai.api_key = os.getenv("OPENAIKEY")

    keywords = [line.strip() for line in open('keywords.csv', 'r')]

    def __init__(self, inText) -> None:
        self.text = inText

    def getSents(self):

        self.sentiPrompt = (
            "i will provide a list of key words and phrases. i will then provide a text. provide sentiment towards each keyword from the text.\n" +
            "keywords=" + str(self.keywords) + "\n" +
            "text=\"" + self.text + "\"\n" +
            "output the sentiment on a scale of -1 to 1. make the output a json serialised python dictionary with names enclosed in double quotes."
        )

        # Request sentiment analysis from GPT-3 in one API call
        # response = openai.Completion.create(
        #     engine="text-davinci-002",
        #     prompt=self.sentiPrompt,
        #     max_tokens=100  # Adjust as needed
        # )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.sentiPrompt}
            ]
        )

        # Extract and structure the sentiment analysis for each keyword
        # sentiments = json.loads(response["choices"][0]["text"])
        sentiments = json.loads(completion["choices"][0]["message"]["content"])
        return sentiments
    


