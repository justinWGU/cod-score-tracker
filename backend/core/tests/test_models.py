from django.test import TestCase
from core.models import Match


# Create your tests here.
# test --parallel.
# test - -keepdb
class MatchTestCase(TestCase):
    def setUp(self):
        Match.objects.create(id=0, leftTeamScore=0, rightTeamScore=0)

    def test_match_object_creation(self): # what we're testing, what the result should be
        match = Match.objects.get(id=0)
        self.assertTrue(isinstance(match, Match))
        self.assertEqual(match.leftTeamScore, 0, "Left team score should be a number 0.")
        self.assertEqual(match.rightTeamScore, 0, "Right team score should be a number 0.")

    def test_object_not_found(self):
        with self.assertRaises(Match.DoesNotExist):
            Match.objects.get(id=1)