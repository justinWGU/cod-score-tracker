from django.test import TestCase
from unittest.mock import patch, MagicMock
from core.services.save_scores import save_scores
from core.models import Match


class TestSaveScores(TestCase):
    def setUp(self):
        pass


    def test_save_scores(self):
        """Assert that function saves correct scores given match_id and scores."""

        # create a Match obj to save and retrieve scores with
        Match.objects.create(id=9)

        # call function to save scores
        scores = {'teamLeft': 99, 'teamRight': 50}
        save_scores(match_id=9, scores=scores)

        # retrieve scores
        match = Match.objects.get(id=9)
        left_scores = match.leftTeamScore
        right_scores = match.rightTeamScore

        # assert scores are the ones saved
        self.assertEqual(left_scores, 99)
        self.assertEqual(right_scores, 50)

