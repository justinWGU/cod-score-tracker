from re import match

from django.test import TestCase
from unittest.mock import MagicMock, patch
from core.services.update_scores import update_from_stream


class TestUpdateFromStream(TestCase):
    def setUp(self):
        pass

    @patch('core.services.update_scores.time')
    @patch('core.services.update_scores.save_scores')
    @patch('core.services.update_scores.extract_scores')
    @patch('core.services.update_scores.take_screenshot')
    def test_stream_calls_proper_functions(self, mock_take_screenshot, mock_extract_scores, mock_save_scores, mock_time):
        """Assert that calls proper functions."""
        mock_take_screenshot.return_value = None

        # mock_scores = MagicMock()
        mock_extract_scores.return_value = 'test scores'
        # mock_scores = 'test scores'

        mock_save_scores.return_value = None

        mock_sleep = MagicMock()
        mock_time.sleep = mock_sleep
        mock_sleep.return_value = None

        # call actual func
        update_from_stream(False, 3, 'test stream url', 5)

        # make assertions
        mock_take_screenshot.assert_called_once_with('test stream url')
        mock_extract_scores.assert_called_once_with(test=False)
        mock_save_scores.assert_called_once_with(match_id=3, scores='test scores')
        mock_sleep.assert_called_once_with(5)

