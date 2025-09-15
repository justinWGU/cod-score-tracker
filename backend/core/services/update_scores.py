import os
import time
import subprocess
from core.services.take_screenshot import take_screenshot
from core.services.extract_scores import extract_scores, gen_random_scores
from core.models import Match
from core.services.get_url import get_url


def save_scores(match_id, scores: dict):
    """ Saves updated match scores to DB."""

    print("Saving scores...")

    scores_left = scores.get('team_left')
    scores_right = scores.get('team_right')

    match = Match.objects.get(id=match_id)
    match.leftTeamScore = scores_left
    match.rightTeamScore = scores_right
    match.save()

    print("Scores saved.")
    

def update_scores(match_id):
    """ Extracts scores from a stream or video and updates the db. """
    
    while True:
        # take a ss from pre-recorded video and generate random scores if testing
        
        direct_stream_url = get_direct_url()
        
        try:
          take_screenshot(direct_stream_url)
          scores = extract_scores()           
          save_scores(match_id, scores)
          time.sleep(2)
            
        except (ValueError, TypeError) as e:
            print(f'Scores did not return as ints in extract_scores: {e}')
            continue
        except Match.DoesNotExist as e:
            print(f'No match with id {match_id} found: {e}')
            return
        except Exception as e:
            print(f'Unknown error ocurred during update_scores loop: {e}')
            return

def update_rand_scores():
  """ Generate and save random scores to the DB. """
  while True:
    scores = gen_random_scores()
    save_scores(1, scores)
    time.sleep(2)
    
  
def get_direct_url():
  try:
    youtube_live_url = os.getenv("STREAM_URL")
    direct_stream_url = get_url(youtube_live_url)
    return direct_stream_url
    
  except subprocess.CalledProcessError as e:
    print("Failed to extract direct URL:", e.stderr)
    return    
  except Exception as e:
    print(f'Could not resolve direct url: {e}')
    return