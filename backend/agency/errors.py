from . import app
from flask import jsonify
from agency.auth.views import AuthError


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
    }), 400


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unable to process request'
    }), 422


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'internal server error'
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        'success': False,
        'error': error.status_code,
        'message': f"{error.error['code']}: {error.error['description']}"
    }), error.status_code
