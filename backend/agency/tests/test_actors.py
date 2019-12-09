import os
import json
import unittest
from agency import app

class ActorsTestCase(unittest.TestCase):
    """This class represents the Actors test case """
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = app
        self.client = self.app.test_client

    def test_get_actors(self):
        actors = [{'name': 'James Doe'}]

        response = self.client().get('/api/v1/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actors'], actors)
        
        