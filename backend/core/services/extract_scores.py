import os
import random
from dotenv import load_dotenv
from google import genai
from ast import literal_eval
from pathlib import Path


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent 
DEFAULT_SCREENSHOT_PATH = BASE_DIR / 'core' / 'services' / 'static' / 'screenshot.jpg'
PROMPT = ('These are screenshots from a competitive e-sports game. Each '
          'team\'s score should appear at the top of each image. Output the scores as a python dictionary. Name the team on the left team_left and the team on the right team_right. Output the dictionary on one line with no formatting white space. Do not add extra characters. If no scoreboard is currently visible at the '
          'top, return each team\'s score as Python data type None.')
BASE_MODEL = 'gemini-1.5-flash'
FALLBACK_MODEL = 'gemini-2.0-flash-lite'


def extract_scores():
    """ Feeds image to genai model and extracts scores in json format. """

    print("Extracting scores...")

    try:
        response = get_response(DEFAULT_SCREENSHOT_PATH, PROMPT, BASE_MODEL)
    except Exception as e:
        print(f'Exception occurred in extract_scores: {e}')
        print('Switching to back up model...')
        response = get_response(DEFAULT_SCREENSHOT_PATH, PROMPT, FALLBACK_MODEL)

    # strip response of unnecessary chars
    start = response.text.find('{')
    end = response.text.find('}')
    scores = response.text[start:end + 1].strip()
    scores = literal_eval(scores) # convert to dict
    scores.team_left = int(scores.team_left)
    scores.team_right = int(scores.team_right)
    print("Extracted scores: ", scores)

    return scores

def get_response(file, PROMPT, model):
    """ Returns gemini response given prompt, image, and model name.v"""

    client = genai.Client(api_key=os.getenv('GEMINI_KEY'))
    file = client.files.upload(file=file)
    response = client.models.generate_content(
        model=model,
        contents=[file, PROMPT])
    client.files.delete(name=file.name)

    return response


def gen_random_scores():
    """ Generates and saves random scores to the DB. """

    print("Extracting mock scores...")
    scores = { 'team_left': random.randint(0,250), 'team_right': random.randint(0,250) }
    print("Mock scores: ", scores)
    return scores    