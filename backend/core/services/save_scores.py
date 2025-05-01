from core.models import Match


def save_scores(match_id, scores):
    """ Saves updated match scores to DB."""

    print("Saving scores...")

    scores_left = scores.get('teamLeft')
    scores_right = scores.get('teamRight')

    try:
        match = Match.objects.get(id=match_id)
        match.leftTeamScore = scores_left
        match.rightTeamScore = scores_right
        match.save()
    except Match.DoesNotExist as dne:
        print(f"No match with id {match_id} found.")
        raise dne
    except Exception as e:
        print("Unknown error occurred while attempting to save match to DB.")
        raise e

    print("Scores updated...")