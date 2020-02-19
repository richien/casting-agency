import json
from flask import Blueprint, jsonify, request, abort
from sqlalchemy import desc

from ..models import Movie, Actor
from .helpers import (
    isValidPostRequest,
    reformat,
    isValidPatchRequest,
    isValidActorId)
from agency.auth.views import requires_auth


movies = Blueprint('movies', __name__)
PER_PAGE = 10


'''
Retrieves a paginated list of movies.
'''
@movies.route('/movies', methods=['GET'])
@requires_auth(permission='get:movies')
def retrieve_movies():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', PER_PAGE, type=int)
    offset = (page - 1) * limit
    try:
        movies = Movie.query.order_by(
            desc(Movie.created_at)).offset(
                offset).limit(
                    limit).all()
        if not movies:
            abort(404)
        data = [movie.format() for movie in movies]
        total_movies = len(Movie.query.all())
        return jsonify({
                'success': True,
                'movies': data,
                'total-movies': total_movies
            }), 200
    except Exception as error:
        raise error


'''
Retrieves a single movie.
'''
@movies.route('/movies/<int:id>', methods=['GET'])
@requires_auth(permission='get:movies')
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


'''
Creates a movie.
'''
@movies.route('/movies', methods=['POST'])
@requires_auth(permission='post:movies')
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


'''
Edits a movie.
'''
@movies.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth(permission='patch:movies')
def edit_movie(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(422)
        data = json.loads(request.data)
        if not isValidPatchRequest(data):
            abort(400)
        for key, value in data.items():
            # if the key is'release-date', reformat the key to 'release_date'
            # which is the correct Movie attribute.
            if key == 'release-date':
                key = 'release_date'
            setattr(movie, key, value)
        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200
    except Exception as error:
        raise error


'''
Deletes a movie.
'''
@movies.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth(permission='delete:movies')
def delete_movie(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(422)
        movie.delete()
        return jsonify({
            'success': True,
            'deleted': id
        }), 200
    except Exception as error:
        raise error


'''
Retrieves a list of actors in a movie.
'''
@movies.route('/movies/<int:id>/actors', methods=['GET'])
@requires_auth(permission='get:actors')
def retrieve_movie_actors(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(404)
        actors = movie.actors
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors],
            'total-actors': len(actors)
        }), 200
    except Exception as error:
        raise error


'''
Adds an actor to a movie.
'''
@movies.route('/movies/<int:id>/actors', methods=['POST'])
@requires_auth(permission='post:actors')
def add_movie_actor(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(404)
        data = json.loads(request.data)
        if not isValidActorId(data):
            abort(400)
        actor = Actor.query.get(data['actor-id'])
        if not actor or actor in movie.actors:
            abort(422)
        movie.add_actor(actor)
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 201
    except Exception as error:
        raise error


'''
Removes an actor from a movie.
'''
@movies.route('/movies/<int:id>/actors', methods=['DELETE'])
@requires_auth(permission='delete:actors')
def remove_actor_from_movie(id):
    try:
        movie = Movie.query.get(id)
        if not movie:
            abort(404)
        data = json.loads(request.data)
        if not isValidActorId(data):
            abort(400)
        actor = Actor.query.get(data['actor-id'])
        if not actor or actor not in movie.actors:
            abort(422)
        movie.delete_actor(actor)
        return jsonify({
            'success': True,
            'deleted': actor.id
        }), 200
    except Exception as error:
        raise error
