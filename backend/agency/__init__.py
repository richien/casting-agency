import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv


app = Flask(__name__)
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')

# Load environment variables
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# Set the API prefix
api_url_prefix = '/api/v1'

# Register blueprints for routes
from .actors.views import actors
from .movies.views import movies


app.register_blueprint(actors, url_prefix=api_url_prefix)
app.register_blueprint(movies, url_prefix=api_url_prefix)