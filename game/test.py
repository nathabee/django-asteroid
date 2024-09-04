from django.urls import reverse
from rest_framework.test import APITestCase

class GameAPITestCase(APITestCase):

    def test_initialize_game(self):
        url = reverse('initialize_game')
        data = {'player_id': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_submit_score(self):
        url = reverse('submit_score')
        data = {'player_id': 5, 'score': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
