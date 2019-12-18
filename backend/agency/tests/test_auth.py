# import os
import json
import unittest
# from flask_sqlalchemy import SQLAlchemy

from agency import app
from agency.tests import mock
# from agency.models import setup_db, Actor, Movie
# from .helpers import get_producer_token

# producer_token = get_producer_token()


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = app
        self.client = self.app.test_client

    def test_get_actors_without_authorization_headers(self):

        response = self.client().get('/api/v1/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.header_missing_response)

    def test_get_actors_with_bearer_missing_from_auth_headers(self):

        response = self.client().get(
            '/api/v1/actors',
            headers={'Authorization': f'{mock.casting_asst_token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.bearer_missing_response)

    def test_get_actors_with_token_missing_from_auth_headers(self):

        response = self.client().get(
            '/api/v1/actors',
            headers={'Authorization': 'Bearer '})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.token_missing_response)

    def test_get_actors_with_invalid_auth_headers(self):
        invalid_header = {
            'Authorization': f'Bearer {mock.casting_asst_token} token'}

        response = self.client().get(
            '/api/v1/actors',
            headers=invalid_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.invalid_auth_header_response)

    def test_get_actors_with_expired_token(self):
        header = {
            'Authorization': f'Bearer {mock.expired_token}'}

        response = self.client().get(
            '/api/v1/actors',
            headers=header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.token_expired_response)

    def test_get_actors_with_invalid_signature_token(self):
        header = {
            'Authorization': f'Bearer {mock.token_with_invalid_signature}'}

        response = self.client().get(
            '/api/v1/actors',
            headers=header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.invalid_signature_response)

    def test_get_actors_with_invalid_claims_in_token(self):
        header = {
            'Authorization': f'Bearer {mock.token_with_invalid_claims}'}

        response = self.client().get(
            '/api/v1/actors',
            headers=header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, mock.invalid_claims_response)
