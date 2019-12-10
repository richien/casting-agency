import os
import unittest
import json
from agency import app


class MoviesTestCase(unittest.TestCase):
    """This class represents the Movies test case """
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = app
        self.client = self.app.test_client

    def test_get_movies(self):
        movies = [{'name': 'The Hatchet'}]

        response = self.client().get('/api/v1/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movies'], movies)

