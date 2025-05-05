import os
import time
from core.services.take_screenshot import take_screenshot, get_url
from core.services.extract_scores import extract_scores
from core.services.save_scores import save_scores


# TODO: add docstrings for parameters
def continuously_update_from_stream(test, match_id, direct_stream_url, wait_time=10):
    """Continuously take a SS from a stream, extract scores, and save them."""

    while True:
        update_from_stream(test, match_id, direct_stream_url, wait_time)


def continuously_update_from_video(test, match_id, direct_stream_url, current_frame=0, wait_time=10, increment=60):
    """Continuously take a SS from a video, save scores, and increment frame pos"""

    current_frame = current_frame
    while True:
        update_from_video(test, match_id, direct_stream_url, current_frame, wait_time)
        current_frame += increment


def update_from_stream(test, match_id, direct_stream_url, wait_time=10):

    print("Getting scores from a stream...")

    # take a SS at the current frame of the livestream
    take_screenshot(direct_stream_url)

    # obtain scores from stream
    scores = extract_scores(test=test)

    save_scores(match_id=match_id, scores=scores)

    time.sleep(wait_time)


def update_from_video(test, match_id, direct_stream_url, current_frame=0, wait_time=10):

    print("Getting scores from a video...")

    # take a SS given the frame pos
    take_screenshot(direct_stream_url, current_frame)

    # produce random scores if test=true
    scores = extract_scores(test)
    print("scores ", scores)

    # prevent None values from being saved into
    left = scores.get('team_left')
    right = scores.get('team_right')
    if left is None or right is None:
        return
    else:
        save_scores(match_id, scores)

    time.sleep(wait_time)


def update_scores(match_id, test=False, live=True):
    """
    Every set interval, take a new screenshot, extract scores from it, and save new
    scores to DB.
    """
    print("called update scores")
    # Get YT URL, extract it, & call appropriate method
    youtube_live_url = os.getenv("STREAM_URL")
    direct_stream_url = get_url(youtube_live_url)

    if live:
        continuously_update_from_stream(test, match_id, direct_stream_url)
    else:
        continuously_update_from_video(test, match_id, direct_stream_url, 1000, 5, 60)
