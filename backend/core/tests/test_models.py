from django.test import TestCase
from core.models import Match

# Create your tests here.

class MatchTestCase(TestCase):
    def setUp(self):
        Match.objects.create(id=0, leftTeamScore=0, rightTeamScore=0)

    def test_match_creation(self):
        match = Match.objects.get(id=0)
        self.assertEqual(match.leftTeamScore, 0, "Left team score should be a number 0.")