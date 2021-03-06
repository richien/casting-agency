missing_header_message = 'invalid_header: Authorization header missing'

bearer_missing_message = '''\
invalid_header: "Bearer" missing from Authorization header'''

token_missing_message = '''\
invalid_header: Token missing from Authorization header'''

invalid_auth_header_message = '''\
invalid_header: Authorization header must be "bearer token"'''

token_expired_message = 'token_expired: Token expired'

invalid_signature_token_message = '''\
invalid_token: Unable to verify token header'''

forbidden_error_message = 'forbidden: Permission not found'

unprocessable_error_message = 'unable to process request'

not_found_error_message = 'resource not found'

bad_request_error_message = 'bad request'

not_allowed_error_message = 'method not allowed'

undecodable_token_message = 'invalid_token: Unable to decode token'

casting_asst_token = '''eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFqYzFOVU\
pCTVRrMFJEYzRSakF6TmpNMlJrVkJSalZETVRBM01rRkJNakl3T0VNNFFrSXpNQSJ9.eyJpc3MiOiJ\
odHRwczovL2Nhc3RpbmcuYXV0aDAuY29tLyIsInN1YiI6IlgwZjRkdjBtRUJKcTNlanB1Q3BESzNUUW\
tvbXJYUm85QGNsaWVudHMiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNTc2NzQ5ODIxLCJle\
HAiOjE1NzY4MzYyMjEsImF6cCI6IlgwZjRkdjBtRUJKcTNlanB1Q3BESzNUUWtvbXJYUm85Iiwic2Nv\
cGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJ\
taXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.FzQ3FhEeOiaRckXdVA1pY1XXYPJ\
YgzLLUQiSVpMBplc77um_92J_hNQqAIx723I0sWXy_H-blwKVfxuIp24A5qL0TslGHcdFccbbJQsx3Q\
mO8wGQHhUUulWwi7UTcxnYjQar8RP-FYfXGXtVFJbElTkO71ZDZON8t8wwsf1DG-DTM5SdLCsm0B_O7\
iipk4TSNuVNoKmjR14cWKlO2Je0cabz94BtK6LKJsKZIkxQZdG73KAO2xzBG2R7Fk3Vk1uxgHqK30At\
xPV5_GbsrpVvDc0wYDvR3LzcQzCfw6GGlUkgzrmvq7S3zfz7I8woQwjQaJnywmUJbw8f\
c4wl1CAjPA'''

expired_token = '''eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFqYzFOVUpCTVR\
rMFJEYzRSakF6TmpNMlJrVkJSalZETVRBM01rRkJNakl3T0VNNFFrSXpNQSJ9.eyJpc3MiOiJodHRw\
czovL2Nhc3RpbmcuYXV0aDAuY29tLyIsInN1YiI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNH\
UzQWcxQGNsaWVudHMiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNTc2NjU1NTUxLCJleHAiO\
jE1NzY3NDE5NTEsImF6cCI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNHUzQWcxIiwic2NvcGUi\
OiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMgcG9zdDphY3RvcnMgcG9zdDptb3ZpZXMgcGF0Y2g6YWN0b3J\
zIHBhdGNoOm1vdmllcyBkZWxldGU6YWN0b3JzIGRlbGV0ZTptb3ZpZXMgZ2V0Om1vdmllYWN0b3JzIG\
dldDphY3Rvcm1vdmllcyBwb3N0Om1vdmllYWN0b3IgZGVsZXRlOm1vdmllYWN0b3IiLCJndHkiOiJjb\
GllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIs\
InBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJ\
kZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDptb3ZpZWFjdG9ycyIsImdldDphY3Rvcm\
1vdmllcyIsInBvc3Q6bW92aWVhY3RvciIsImRlbGV0ZTptb3ZpZWFjdG9yIl19.sB4d4rilN6WHC999\
i3o4ETkOgIawkqVP5J_LfsEdYSpAQxCYrtrWa_cr9sO9tx5u7lHBkcna5dmUk3bV4U6WTTcpjbCDkX\
v_S2LWNuFEJok8IzjgIeFwCaL-yamiXJ7GZ4LFluU5xRkx9Yo4O17m1KJvjFK_KeLAKr2Niu5R\
m_MN_4bRARkUohHIo5KODycfaoV21QMPKLTI-xYWRmsBfEfA6gy0FKVjzXLFNljXaag0YBAqry\
FuTeHuKNSRKeetf8BYZ3j6JWKL914yo9bjQyFIJ6uGnpmsDx-aeVy5WBQH3aBw17QIJwVcaqI\
dyleW2O9qVAakEs0D-lGMWaDImw'''

token_with_invalid_signature = '''eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI\
6IlFqYzFOVUpCTVRrMFJEYzRSakF6TmpNMlJrVkJSalZETVRBM01rRkJNakl3T0VNNFFrSXpNQSJ\
9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmcuYXV0aDAuY29tLyIsInN1YiI6IlgwZjRkdjBtRUJKcT\
NlanB1Q3BESzNUUWtvbXJYUm85QGNsaWVudHMiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0I\
joxNTc2NzQ5ODIxLCJleHAiOjE1NzY4MzYyMjEsImF6cCI6IlgwZjRkdjBtRUJKcTNlanB1Q3BES\
zNUUWtvbXJYUm85Iiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMiLCJndHkiOiJjbGllb\
nQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcy\
JdfQ.FzQ3FhEeOiaRckXdVA1pY1XXYPJYgzLLUQiSVpMBplc77um_92J_hNQqAIx723I0sW\
Xy_H-blwKVfxuIp24A5qL0TslGHcdFccbbJQsx3QmO8wGQHhUUulWwi7UTcxnYjQar\
8RP-FYfXGXtVFJbElTkO71ZDZON8t8wwsf1DG-DTM5SdLCsm0B_O7iipk4TSNuVNoKmjR14cWKlO2\
Je0cabz94BtK6LKJsKZIkxQZdG73KAO2xzBG2R7Fk3Vk1uxgHqK30AtxPV5_GbsrpVvDc0wYDvR3L\
zcQzCfw6GGlUkgzrmvq7S3zfz7I8woQwjQaJnywmUJbw8fc4wl1CAjP'''

undecodable_token = '''eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFqYzFOVUpCTVRrMFJEYzRSakF6TmpNMlJrVkJSalZETVRBM01rRkJNakl3T0VNNFFrSXpNQSJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmcuYXV0aDAuY29tLyIsInN1YiI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNHUzQWcxQGNsaWVudHMiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNTc2ODIwNDc2LCJleHAiOjE1NzY5MDY4NzYsImF6cCI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNHUzQWcxIiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMgcG9zdDphY3RvcnMgcG9zdDptb3ZpZXMgcGF0Y2g6YWN0b3JzIHBhdGNoOm1vdmllcyBkZWxldGU6YWN0b3JzIGRlbGV0ZTptb3ZpZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyJdfQ.x6a-YmjpCvXXH9B_YRzY5ehJQXMuD7sF8JK43AO7Mb_yZlgtfIfvsGB_VnAfpEnAJWzk_0TFMa9gOiiXRlssWih_lgK-dxcKEcBlYHVntwXu4fqCjFbNeRerqRVli1Mvq3s026EyfkxCk3hcLse6Hk6iQkgcXAZeqEhISEG_tsOi3A_lAkI97IdFpNnYCxYg6sqq1w9IdfveU0rxw9lNZE75DQpfLGX55-ayKixMMJd18t8jJz9EmIUVjm6ZHrjSJH4b4qUg2bt5DT7Rbn8BpFyBDmTkvfR9MfOTc_zvEneb2Cxu9tHBKv5VpMz-i09qiJRRxOQq2woRAGZxW3wjbweyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFqYzFOVUpCTVRrMFJEYzRSakF6TmpNMlJrVkJSalZETVRBM01rRkJNakl3T0VNNFFrSXpNQSJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmcuYXV0aDAuY29tLyIsInN1YiI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNHUzQWcxQGNsaWVudHMiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNTc2NjU1NTUxLCJleHAiOjE1NzY3NDE5NTEsImF6cCI6IldzaXRUVWhzeU9hekZJd3V2ZU9Hc3RyeXYwNHUzQWcxIiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMgcG9zdDphY3RvcnMgcG9zdDptb3ZpZXMgcGF0Y2g6YWN0b3JzIHBhdGNoOm1vdmllcyBkZWxldGU6YWN0b3JzIGRlbGV0ZTptb3ZpZXMgZ2V0Om1vdmllYWN0b3JzIGdldDphY3Rvcm1vdmllcyBwb3N0Om1vdmllYWN0b3IgZGVsZXRlOm1vdmllYWN0b3IiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDptb3ZpZWFjdG9ycyIsImdldDphY3Rvcm1vdmllcyIsInBvc3Q6bW92aWVhY3RvciIsImRlbGV0ZTptb3ZpZWFjdG9yIl19.sB4d4rilN6WHC999i3o4ETkOgIawkqVP5J_LfsEdYSpAQxCYrtrWa_cr9sO9tx5u7lHBkcna5dmUk3bV4U6WTTcpjbCDkXv_S2LWNuFEJok8IzjgIeFwCaL-yamiXJ7GZ4LFluU5xRkx9Yo4O17m1KJvjFK_KeLAKr2Niu5Rm_MN_4bRARkUohHIo5KODycfaoV21QMPKLTI-xYWRmsBfEfA6gy0FKVjzXLFNljXaag0YBAqryFuTeHuKNSRKeetf8BYZ3j6JWKL914yo9bjQyFIJ6uGnpmsDx-aeVy5WBQH3aBw17QIJwVcaqIdyleW2O9qVAakEs0D-lGMWaDImw'''  # noqa

bad_request_error_response = {
                                'success': False,
                                'error': 400,
                                'message': bad_request_error_message
                            }

header_missing_response = {
                                'success': False,
                                'error': 401,
                                'message': missing_header_message
                            }

bearer_missing_response = {
                                'success': False,
                                'error': 401,
                                'message': bearer_missing_message
                            }

token_missing_response = {
                                'success': False,
                                'error': 401,
                                'message': token_missing_message
                            }

token_expired_response = {
                                'success': False,
                                'error': 401,
                                'message': token_expired_message
                            }

invalid_auth_header_response = {
                                'success': False,
                                'error': 401,
                                'message': invalid_auth_header_message
                            }

invalid_signature_response = {
                                'success': False,
                                'error': 401,
                                'message': invalid_signature_token_message
                            }

undecodable_token_response = {
                                'success': False,
                                'error': 401,
                                'message': undecodable_token_message
                            }

forbidden_error_response = {
                                'success': False,
                                'error': 403,
                                'message': forbidden_error_message
                            }

not_found_error_response = {
                                'success': False,
                                'error': 404,
                                'message': not_found_error_message
                            }

not_allowed_error_response = {
                                'success': False,
                                'error': 405,
                                'message': not_allowed_error_message
                            }

unprocessable_error_response = {
                                'success': False,
                                'error': 422,
                                'message': unprocessable_error_message
                            }

actor = {
            'id': '',
            'name': '',
            'age': '',
            'gender': '',
            'created-at': '',
            'updated-at': ''
        }

movie = {
            'id': '',
            'title': '',
            'release-date': '',
            'created-at': '',
            'updated-at': ''
        }
