import json
from flask import Blueprint, jsonify, abort, request

from ..models import Actor
from .helpers import isValidPostRequest, isValidPatchRequest
from ..auth.views import requires_auth


actors = Blueprint('actors', __name__)
PER_PAGE = 10


'''
Retrieves a paginated list of actors.
'''
@actors.route('/actors', methods=['GET'])
@requires_auth(permission='get:actors')
def retrieve_actors():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', PER_PAGE, type=int)
    offset = (page - 1) * limit
    try:
        actors = Actor.query.offset(offset).limit(limit).all()
        if not actors:
            abort(404)
        data = [actor.format() for actor in actors]
        total_actors = len(Actor.query.all())
        return jsonify({
                'success': True,
                'actors': data,
                'total-actors': total_actors
            }), 200
    except Exception as error:
        raise error


'''
Retrieves a single actor by their ID.
'''
@actors.route('/actors/<int:id>', methods=['GET'])
@requires_auth(permission='get:actors')
def retrieve_actor(id):
    try:
        actor = Actor.query.get(id)
        if not actor:
            abort(404)
        return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
    except Exception as error:
        raise error


'''
Creates a new actor.
'''
@actors.route('/actors', methods=['POST'])
@requires_auth(permission='post:actors')
def add_actor():
    try:
        data = json.loads(request.data)
        if not isValidPostRequest(data):
            abort(400)
        actor = Actor(**data)
        actor.insert()
        return jsonify({
                'success': True,
                'actor': actor.format()
            }), 201
    except Exception as error:
        raise error


'''
Edits an actor's details.
'''
@actors.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth(permission='patch:actors')
def edit_actor(id):
    try:
        actor = Actor.query.get(id)
        if not actor:
            abort(422)
        data = json.loads(request.data)
        if not isValidPatchRequest(data):
            abort(400)
        for key, value in data.items():
            setattr(actor, key, value)
        actor.update()
        return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
    except Exception as error:
        raise error


'''
Deletes an actor.
'''
@actors.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth(permission='delete:actors')
def delete_actor(id):
    try:
        actor = Actor.query.get(id)
        if not actor:
            abort(422)
        actor.delete()
        return jsonify({
                'success': True,
                'deleted': actor.id
            }), 200
    except Exception as error:
        raise error


'''
Retrieves an actor's movies.
'''
@actors.route('/actors/<int:id>/movies', methods=['GET'])
@requires_auth(permission='get:movies')
def retrieve_actor_movies(id):
    try:
        actor = Actor.query.get(id)
        if not actor:
            abort(404)
        movies = [movie.format() for movie in actor.movies]
        return jsonify({
            'success': True,
            'movies': movies,
            'total-movies': len(movies)
        }), 200
    except Exception as error:
        raise error
