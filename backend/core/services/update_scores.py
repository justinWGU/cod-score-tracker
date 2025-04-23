from take_screenshot import take_screenshot
from extract_scores import extract_scores
import time

def update_scores():
    """
    Every 5 seconds, take a new screenshot, extract scores, and save new
    scores to DB.
    """

    # continuously run program
    while True:
        take_screenshot()
        scores = extract_scores()

        # save scores to DB
        scores_left = scores.get('teamLeft')
        scores_right = scores.get('teamRight')

        # save updated match scores in DB
        match = Match.objects.get(id=1)
        match.leftTeamScore = scores_left
        match.rightTeamScore = scores_right
        match.save()

        # wait 5 secs
        time.sleep(10)