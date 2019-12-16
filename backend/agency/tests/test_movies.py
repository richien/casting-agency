import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from agency import app
from agency.models import setup_db, Movie, Actor


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
            for actor in Actor.query.all():
                actor.delete()
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
        self.assertEqual(data['total-movies'], 1)

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

    def test_edit_movie_with_invalid_field(self):
        release_date = '2020-13-01'
        # 'release-dates' is an invalid field
        movie = {
            'release-dates': release_date
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

    def test_delete_movie_with_success_response(self):

        response = self.client().delete(f'/api/v1/movies/{self.movie_id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('success')
        self.assertEqual(data['deleted'], self.movie_id)

    def test_delete_movie_with_invalid_id(self):
        movie_id = 0  # invalid movie_id

        response = self.client().delete(f'/api/v1/movies/{movie_id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unable to process request')

    def test_get_actors_in_a_movie(self):
        with self.app.app_context():
            actor = Actor(name="James Doe", age=23, gender="male")
            actor.movies = [self.movie]
            actor.insert()

        response = self.client().get(f'/api/v1/movies/{self.movie_id}/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['actors'], list)
        self.assertEqual(data['total-actors'], 1)

    def test_get_movie_actors_with_invalid_movie_id(self):
        movie_id = 0  # invalid movie id

        response = self.client().get(f'/api/v1/movies/{movie_id}/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_add_actor_to_movie(self):
        actor_id = ''
        with self.app.app_context():
            actor = Actor(name="James Doe", age=23, gender="male")
            actor.insert()
            actor_id = actor.id

        response = self.client().post(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['id'], actor_id)

    def test_add_actor_to_movie_with_invalid_movie_id(self):
        movie_id = 0  # invalid movie id
        actor_id = ''
        with self.app.app_context():
            actor = Actor(name="James Doe", age=23, gender="male")
            actor.insert()
            actor_id = actor.id

        response = self.client().post(
            f'/api/v1/movies/{movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_add_actor_to_movie_with_invalid_actor_id(self):
        actor_id = 0  # invalid actor ID

        response = self.client().post(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unable to process request')

    def test_add_actor_to_movie_with_invalid_ID_key_in_request_body(self):
        # the key 'actor_id' is invalid
        response = self.client().post(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor_id': 1}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_add_actor_to_movie_with_string_actor_id_in_request_body(self):
        actor_id = "23eff"
        response = self.client().post(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_remove_actor_from_movie(self):
        actor_id = ''
        with self.app.app_context():
            actor = Actor(name="James Doe", age=23, gender="male")
            actor.insert()
            actor_id = actor.id
            movie = Movie.query.get(self.movie_id)
            movie.add_actor(actor)

        response = self.client().delete(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], actor_id)

    def test_remove_actor_with_invalid_movie_id(self):
        movie_id = 0  # invalid movie id
        actor_id = ''
        with self.app.app_context():
            actor = Actor(name="James Doe", age=23, gender="male")
            actor.insert()
            actor_id = actor.id

        response = self.client().delete(
            f'/api/v1/movies/{movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_remove_actor_with_invalid_actor_id(self):
        actor_id = 0  # invalid actor ID

        response = self.client().delete(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor-id': actor_id}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unable to process request')

    def test_remove_actor_with_invalid_ID_key_in_request_body(self):
        # the key 'actor_id' is invalid
        response = self.client().delete(
            f'/api/v1/movies/{self.movie_id}/actors',
            content_type='application/json',
            data=json.dumps({'actor_id': 1}))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')
