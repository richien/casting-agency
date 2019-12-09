from flask import Blueprint, jsonify


actors = Blueprint('actors', __name__)

@actors.route('/actors')
def hello():
    return jsonify({
        'success': True,
        'actors': [{'name': 'James Doe'}]
    }), 200