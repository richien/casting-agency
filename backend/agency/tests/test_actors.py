import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from agency import app
from agency.models import setup_db, Actor


class ActorsTestCase(unittest.TestCase):
    """This class represents the Actors test case """
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = app
        self.client = self.app.test_client
        database_path = os.getenv('TEST_DATABASE_URI')
        setup_db(self.app, database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
            # Add an actor
            self.actor = Actor(name="James Doe", age=23, gender="male")
            self.actor.insert()

    def tearDown(self):
        with self.app.app_context():
            self.actor.delete()

    def test_get_actors_with_successful_response(self):
        actor = {'name': 'James Doe', 'age': 23, 'gender': 'male'}

        response = self.client().get('/api/v1/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(actor['name'], data['actors'][0]['name'])
        self.assertEqual(actor['age'], data['actors'][0]['age'])
        self.assertEqual(actor['gender'], data['actors'][0]['gender'])
        self.assertEqual(data['total_actors'], 1)

    def test_get_actors_with_failure_response(self):
        page = 100  # This page doesn't exist
        response = self.client().get(f'/api/v1/actors?page={page}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')