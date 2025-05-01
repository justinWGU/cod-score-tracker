from unittest.mock import patch
from rest_framework.test import APISimpleTestCase, APITestCase
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from core.models import Match
from core.views import update_scores_view
from django.urls import resolve, reverse


class TestViews(APISimpleTestCase): # does not create a virtual db

    def test_url_routes_to_update_scores_view(self):
        resolver = resolve('/api/update-scores/') # obj to determine what view the url resolves to
        self.assertEqual(resolver.func, update_scores_view)



class TestIntegration(APITestCase):

    def setUp(self):
        match = Match.objects.create(id=1)
        match.rightTeamScore = 100
        match.leftTeamScore = 101
        match.save()

    @patch('core.services.update_scores.extract_scores')
    @patch('core.services.update_scores.take_screenshot_from_stream')
    @patch('core.services.update_scores.get_stream_url')
    def test_data_is_updated(self, mock_get_stream_url, mock_take_screenshot_from_stream, mock_extract_scores):
        """
        Assert that api call starts correct methods and updates correct data
        to DB.
        """

        mock_get_stream_url.return_value = 'mock_url'
        mock_take_screenshot_from_stream.return_value = None
        mock_extract_scores.return_value = {'teamLeft': 69, 'teamRight': 67}

        # make the api call
        path = reverse('update-scores')
        response = self.client.get(path=path, query_params={'id': '1', 'test': 'false', 'live': 'true'})

        # get data that should have been saved in the DB
        match = Match.objects.get(id=1)
        score_left = match.leftTeamScore
        score_right = match.rightTeamScore

        # assert
        self.assertEqual(response.status_code, HTTP_200_OK)
        mock_get_stream_url.assert_called_once()
        mock_take_screenshot_from_stream.assert_called_once_with('mock_url')
        self.assertEqual(score_right, 67)
        self.assertEqual(score_left, 69)


    def test_get_data(self):
        """ Assert that data is properly returned using get_data endpoint."""

        # make the api call
        path = reverse('get-scores')
        response = self.client.get(path=path, query_params={'id': '1'})

        # get response data
        left_team_score = response.data.get('leftTeamScore')
        right_team_score = response.data.get('rightTeamScore')

        # assert data
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(right_team_score, 100)
        self.assertEqual(left_team_score, 101)
