from django.test import TestCase
from unittest.mock import Mock, MagicMock, patch
from core.services.update_scores import update_from_video


class TestUpdateFromVideo(TestCase):

    @patch('core.services.update_scores.time')
    @patch('core.services.update_scores.save_scores')
    @patch('core.services.update_scores.extract_scores')
    @patch('core.services.update_scores.take_screenshot')
    def test_update_from_video_calls_functions_correctly(self, mock_take_screenshot, mock_extract_scores, mock_save_scores, mock_time):
        """Assert that this function calls all functions with correct arguments."""

        # mock functions
        mock_take_screenshot.return_value = None
        mock_extract_scores.return_value = {'mock scores': 100}
        mock_save_scores.return_value = None
        mock_time.sleep.return_value = None

        # call real function
        update_from_video(test=True, match_id=5, direct_stream_url='mock stream url', current_frame=100, wait_time=5)# update_from_video(test, match_id, direct_stream_url, current_frame=0, wait_time=10, increment=60):

        # assert
        mock_take_screenshot.assert_called_once_with('mock stream url', 100)
        mock_extract_scores.assert_called_once_with(True)
        mock_save_scores.assert_called_once_with(5, {'mock scores': 100})
        mock_time.sleep.assert_called_once_with(5)

