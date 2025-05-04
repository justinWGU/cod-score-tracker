from core.models import Match


def save_scores(match_id, scores: dict):
    """ Saves updated match scores to DB."""

    print("Saving scores...")

    scores_left = scores.get('teamLeft')
    scores_right = scores.get('teamRight')

    match = Match.objects.get(id=match_id)
    match.leftTeamScore = scores_left
    match.rightTeamScore = scores_right
    match.save()

    print("Scores updated...")