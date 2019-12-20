import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from .models import setup_db


app = Flask(__name__)

# Setup CORS
CORS(app)

# Load environment variables
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# Setup the database
setup_db(app)

# Set the API prefix
api_url_prefix = '/api/v1'

# Import error handlers
from . import errors # noqa

# Register blueprints for routes
from .actors.views import actors # noqa
from .movies.views import movies # noqa


app.register_blueprint(actors, url_prefix=api_url_prefix)
app.register_blueprint(movies, url_prefix=api_url_prefix)
