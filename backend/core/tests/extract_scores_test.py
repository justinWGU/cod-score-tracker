from django.test import TestCase
from unittest.mock import patch, Mock, MagicMock

from google.genai import Client

from core.services.extract_scores import extract_scores_test, extract_scores
from dotenv import load_dotenv
import os


class TestExtractScores(TestCase):

    def setUp(self):
        # load env variables
        load_dotenv()


    @patch('core.services.extract_scores.genai.Client')
    def test_extract_scores(self, mock_client_class):
        """Assert extract_scores calls correct functions and returns dictionary."""

        # mock Client class to return a MagicMock instance
        mock_client = mock_client_class.return_value

        # mock files.upload() to return a file obj
        mock_file = MagicMock()
        mock_client.files.upload.return_value = mock_file
        mock_file.name = 'mock_file'

        # mock generate_content to return a response obj
        mock_response = MagicMock()
        mock_client.models.generate_content.return_value = mock_response # generate_content returns an obj
        mock_response.text = "{'team_left': 23, 'team_right': 42}" # assign directly to text since it's an attr
        mock_client.files.delete.return_value = None

        # call actual method
        scores = extract_scores()

        # assert
        self.assertTrue(isinstance(scores, dict))
        self.assertEqual(scores, {'team_left': 23, 'team_right': 42})


    @patch('core.services.extract_scores.extract_scores_test')
    def test_extract_scores_with_test_equals_true(self, mock_extract_scores_test):
        """Assert that passing test=True will call the test function."""


        # mock external functions
        mock_extract_scores_test.return_value = None

        # call extract_scores w/ test=True
        extract_scores(test=True)

        # assure extract_scores_test was called
        mock_extract_scores_test.assert_called_once()
