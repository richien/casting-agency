import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import date

from agency import app
from agency.models import setup_db, Movie


class MoviesTestCase(unittest.TestCase):
    """This class represents the Movies test case """
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = app
        self.client = self.app.test_client
        database_path = os.getenv('TEST_DATABASE_URI')
        setup_db(self.app, database_path)
        self.movie_id = ''
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
            # Add a movie
            self.movie = Movie(
                title='The Hatchet',
                release_date=date(2020, 12, 11)
            )
            self.movie.insert()
            self.movie_id = self.movie.id

    def tearDown(self):
        with self.app.app_context():
            self.db.session.query(Movie).delete()
            self.db.session.commit()

    def test_get_movies_with_successfull_response(self):
        release_date = date(2020, 12, 11)
        movie = {
            'title': 'The Hatchet',
            'release-date': release_date.strftime("%A, %d %B %Y")
        }

        response = self.client().get('/api/v1/movies?page=1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movies'][0]['title'], movie['title'])
        self.assertEqual(
            data['movies'][0]['release-date'], movie['release-date']
        )
        self.assertEqual(data['total_movies'], 1)

    def test_get_movies_with_invalid_page_number(self):
        page = 100  # This page doesn't exist
        response = self.client().get(f'/api/v1/movies?page={page}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')
