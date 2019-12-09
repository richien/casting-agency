from flask import Blueprint, jsonify


movies = Blueprint('movies', __name__)

@movies.route('/movies')
def hello():
    return jsonify({
        'success': True,
        'movies': [{'name': 'The Hatchet'}]
    }), 200