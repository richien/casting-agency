import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
                release_date=datetime(2020, 12, 11)
            )
            self.movie.insert()
            self.movie_id = self.movie.id

    def tearDown(self):
        with self.app.app_context():
            self.db.session.query(Movie).delete()
            self.db.session.commit()

    def test_get_movies_with_successfull_response(self):
        release_date = datetime(2020, 12, 11)
        movie = {
            'title': 'The Hatchet',
            'release-date': release_date.isoformat()
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

    def test_get_movie_with_successfull_response(self):
        release_date = datetime(2020, 12, 11)
        movie = {
            'id': self.movie_id,
            'title': 'The Hatchet',
            'release-date': release_date.isoformat()
        }

        response = self.client().get(f'/api/v1/movies/{self.movie_id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie'], movie)

    def test_get_movie_with_invalid_movie_id(self):
        movie_id = 0  # invalid movie ID

        response = self.client().get(f'/api/v1/movies/{movie_id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_add_movie_with_successfull_response(self):
        release_date = datetime(2020, 2, 9)
        movie = {
            'title': 'Above The Storm',
            'release-date': release_date.isoformat()
        }

        response = self.client().post(
                    '/api/v1/movies',
                    content_type='application/json',
                    data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie']['title'], movie['title'])
        self.assertEqual(data['movie']['release-date'], movie['release-date'])

    def test_add_movie_with_invalid_date_string(self):
        release_date = "2020-13-01T00:00:00"  # invalid month 13 in date
        movie = {
            'title': 'Above The Storm',
            'release-date': release_date
        }

        response = self.client().post(
                    'api/v1/movies',
                    content_type='application/json',
                    data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_add_movie_with_empty_title_string(self):
        release_date = datetime(2020, 2, 9)
        movie = {
            'title': '',
            'release-date': release_date.isoformat()
        }

        response = self.client().post(
                    'api/v1/movies',
                    content_type='application/json',
                    data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_add_movie_with_missing_title_string(self):
        release_date = datetime(2020, 2, 9)
        movie = {
            'release-date': release_date.isoformat()
        }

        response = self.client().post(
                    'api/v1/movies',
                    content_type='application/json',
                    data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_edit_movie_with_successfull_response(self):
        release_date = datetime(2020, 2, 9)
        movie = {
            'release-date': release_date.isoformat()
        }

        response = self.client().patch(
                        f'/api/v1/movies/{self.movie_id}',
                        content_type='application/json',
                        data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie']['id'], self.movie_id)
        self.assertEqual(data['movie']['release-date'], movie['release-date'])

    def test_edit_movie_with_invalid_movie_id(self):
        movie_id = 0  # invalid movie ID
        release_date = datetime(2020, 2, 9)
        movie = {
            'release-date': release_date.isoformat()
        }

        response = self.client().patch(
                        f'/api/v1/movies/{movie_id}',
                        content_type='application/json',
                        data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unable to process request')

    def test_edit_movie_with_empty_title_string(self):
        movie = {
            'title': ''
        }

        response = self.client().patch(
                        f'/api/v1/movies/{self.movie_id}',
                        content_type='application/json',
                        data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_edit_movie_with_invalid_date(self):
        release_date = '2020-13-01'  # date with invalid month 13
        movie = {
            'release-date': release_date
        }

        response = self.client().patch(
                        f'/api/v1/movies/{self.movie_id}',
                        content_type='application/json',
                        data=json.dumps(movie))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')
