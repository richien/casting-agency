import os
import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
ALGORITHMS = os.getenv('ALGORITHMS')
API_AUDIENCE = os.getenv('API_AUDIENCE')
JWKS_URL = os.getenv('JWKS_URL')


class AuthError(Exception):
    '''AuthError Exception.

    A standardized way to communicate authentication errors.
    '''
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_from_auth_header():
    '''Checks for the correct authorization header.

    Returns:
        str: The token string.
    '''
    headers = request.headers.get('Authorization', None)
    if not headers:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization header missing'
            }, 401)
    parts = headers.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
                'code': 'invalid_header',
                'description': '"Bearer" missing from Authorization header'
            }, 401)
    elif len(parts) == 1:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Token missing from Authorization header'
            }, 401)
    elif len(parts) > 2:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization header must be "bearer token"'
            }, 401)
    token = parts[1]
    return token


def get_rsa_key(token):
    '''Checks the JSON Web Key Set(jwks) for an rsa key.

    Uses the key ID stored in the token header.
    Args:
        token(str): The token string.
    Returns:
        dict: The rsa key.
    '''
    JWKS_URL = os.getenv('JWKS_URL')
    try:
        jsonurl = urlopen(JWKS_URL)
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        if 'kid' not in unverified_header:
            raise AuthError({
                    'code': 'invalid_header',
                    'description': '"kid" missing from token header'
                }, 401)
        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }
        if not rsa_key:
            raise AuthError({
                    'code': 'invalid_key',
                    'description': 'Unable to find the appropriate key'
                }, 401)
        return rsa_key
    except Exception:
        raise AuthError({
                'code': 'invalid_token',
                'description': 'Unable to verify token header'
            }, 401)


def verify_decode_jwt(token):
    '''Verifies and decodes the jwt token.

    Args:
        token (str): The token string.
    Returns:
        dict: The token payload.
    '''
    rsa_key = get_rsa_key(token)
    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f'https://{AUTH0_DOMAIN}/'
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired'
            }, 401)
    except jwt.JWTClaimsError:
        raise AuthError({
                'code': 'invalid_claims',
                'description': 'Please check the issuer and audience'
            }, 401)
    except Exception:
        raise AuthError({
                'code': 'invalid_token',
                'description': 'Unable to decode token'
            }, 401)


def check_permissions(permission, payload):
    '''Checks whether a token payload contains the supplied permissions.

    Args:
        permission (str): The permission string.
        payload (dict): The token payload.
    Returns:
        bool: True is successfull.
    '''
    if 'permissions' not in payload:
        raise AuthError({
                'code': 'invalid_payload',
                'description': 'Permissions not included in JWT payload'
            }, 400)
    if permission not in payload['permissions']:
        raise AuthError({
                'code': 'forbidden',
                'description': 'Permission not found'
            }, 403)
    return True


def requires_auth(permission=''):
    '''Implements authentication and authorization.

    Args:
        permission (str): The permission string.
    Returns:
        func: decorator function.
    '''
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_from_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator
