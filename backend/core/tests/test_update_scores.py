from core.services import update_scores
from core.models import Match
from core.services.update_scores import update_scores
from django.test import TestCase
from unittest.mock import patch


class UpdateScoresTestCase(TestCase):
    def setUp(self):
        Match.objects.create(id=5)


    @patch('core.services.update_scores.continuously_update_from_video')
    @patch('core.services.update_scores.continuously_update_from_stream')
    @patch('core.services.update_scores.get_url')
    def test_that_update_from_stream_is_called_from_update_scores(self, mock_get_url, mock_continuously_update_from_stream, mock_continuously_update_from_video):
        """
        Assert that the continuously_update_from_video method is called given live=False.
        """

        mock_get_url.return_value = None
        mock_continuously_update_from_stream.return_value = None
        mock_continuously_update_from_video.return_value = None

        update_scores(match_id=5, live=False)

        mock_continuously_update_from_stream.assert_not_called()
        mock_continuously_update_from_video.assert_called_once()



    @patch('core.services.update_scores.continuously_update_from_video')
    @patch('core.services.update_scores.continuously_update_from_stream')
    @patch('core.services.update_scores.get_url')
    def test_that_update_from_stream_is_called_from_update_scores(self, mock_get_url, mock_continuously_update_from_stream, mock_continuously_update_from_video):
        """
        Assert that the update_scores_stream method is called given live=True.
        """

        mock_get_url.return_value = None
        mock_continuously_update_from_stream.return_value = None
        mock_continuously_update_from_video.return_value = None

        update_scores(match_id=5, live=True)

        mock_continuously_update_from_video.assert_not_called()
        mock_continuously_update_from_stream.assert_called_once()

