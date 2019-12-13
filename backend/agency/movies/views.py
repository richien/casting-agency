import json
from flask import Blueprint, jsonify, request, abort

from ..models import Movie
from .helpers import isValidPostRequest, reformat


movies = Blueprint('movies', __name__)
PER_PAGE = 10


@movies.route('/movies', methods=['GET'])
def retrieve_movies():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', PER_PAGE, type=int)
    offset = (page - 1) * limit
    try:
        movies = Movie.query.offset(offset).limit(limit).all()
        if not movies:
            abort(404)
        data = [movie.format() for movie in movies]
        total_movies = len(Movie.query.all())
        return jsonify({
                'success': True,
                'movies': data,
                'total_movies': total_movies
            }), 200
    except Exception as error:
        raise error


@movies.route('/movies/<int:id>', methods=['GET'])
def retrieve_movie(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(404)
        return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
    except Exception as error:
        raise error


@movies.route('/movies', methods=['POST'])
def add_movie():
    try:
        data = json.loads(request.data)
        if not isValidPostRequest(data):
            abort(400)
        data = reformat(data)
        movie = Movie(**data)
        movie.insert()
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 201
    except Exception as error:
        raise error
