import os
import random
from dotenv import load_dotenv
from google import genai
from ast import literal_eval


load_dotenv()

def extract_scores(test=False):
    """Feeds image to genai model and extracts scores in json format."""
    if test:
        return extract_scores_test()

    print("Extracting scores...")

    file = '/Users/justin/projects/score-tracker/backend/core/services/static/screenshot.jpg'

    prompt = ('These are screenshots from a competitive e-sports game. Each '
              'team\'s score should appear at the top of each image. Output the scores as a python dictionary. Name the team on the left team_left and the team on the right team_right. Output the dictionary on one line with no formatting white space. Do not add extra characters. If no scoreboard is currently visible at the '
              'top, return each team\'s score as Python data type None.')

    try:
        response = get_response(file, prompt, 'gemini-1.5-flash')
    except Exception as e:
        print(f'Exception occurred in extract_scores: {e}')
        print('Switching to back up model.')
        response = get_response(file, prompt, 'gemini-2.0-flash-lite')

    # strip response of unnecessary chars
    # TODO: Find alternative lib to transform response to dict
    start = response.text.find('{')
    end = response.text.find('}')
    scores = response.text[start:end + 1].strip()
    scores = literal_eval(scores) # convert to dict
    print("Extracted scores: ", scores)

    return scores


def get_response(file, prompt, model):
    """Gets & returns gemini response given prompt, image, and model name."""

    # init gemini client
    client = genai.Client(api_key=os.getenv('GEMINI_KEY'))

    file = client.files.upload(file=file)

    response = client.models.generate_content(
        model=model,
        contents=[file, prompt])

    client.files.delete(name=file.name)

    return response


def extract_scores_test():
    """Mock extraction method that returns random scores for each team."""

    print("Mock extracting scores...")
    scores = { 'team_left': random.randint(0,250), 'team_right': random.randint(0,250) }
    print("Mock scores: ", scores)
    return scores
