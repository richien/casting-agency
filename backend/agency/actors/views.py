from flask import Blueprint, jsonify, abort, request
from ..models import Actor


actors = Blueprint('actors', __name__)
PER_PAGE = 10


@actors.route('/actors', methods=['GET'])
def retrieve_actors():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', PER_PAGE, type=int)
    offset = (page - 1) * limit
    try:
        actors = Actor.query.offset(offset).limit(limit).all()
        if not actors:
            abort(404)
        data = [actor.format() for actor in actors]
        return jsonify({
                'success': True,
                'actors': data,
                'total_actors': len(data)
            }), 200
    except Exception as error:
        raise error


@actors.route('/actors/<int:id>', methods=['GET'])
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
