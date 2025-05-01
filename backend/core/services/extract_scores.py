import os
import random
from dotenv import load_dotenv
from google import genai


load_dotenv()

def extract_scores(test=False):
    """Feeds image to genai model and extracts scores in json format."""
    if test:
        extract_scores_test()
        return

    print("Extracting scores...")
    # init gemini client
    client = genai.Client(api_key=os.getenv('GEMINI_KEY'))

    file = client.files.upload(file='static/screenshot.jpg')

    # prompt gemini model to identify scores and output them in json
    prompt = ('These are screenshots from a competitive e-sports game. Each '
              'team\'s score should appear at the top of each image. Your job is '
              'to output the scores that you see as a python dictionary in the '
              'following {format}. If no scoreboard is currently visible on the '
              'image, return each team\'s score as Python data type None.'
              'TeamLeft is the team whose score appears on the left. TeamRight '
              'is the team whose score appears on the right. '
              '$format = {teamLeft: $SCORE, teamRight: $SCORE}')
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=[file, prompt])
    client.files.delete(name=file.name)

    # remove only the json format from response
    # TODO: Look for lib that converts to python dict
    start = response.text.find('{')
    end = response.text.find('}')
    json = response.text[start:end + 1]
    print('Response:', json)

    return json


def extract_scores_test():
    """Mock extraction method that returns random scores for each team."""

    print("Mock extracting scores...")
    return { "teamLeft": random.randint(0,250), "teamRight": random.randint(0,250) }
