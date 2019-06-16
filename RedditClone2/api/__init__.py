import praw
from flask import Blueprint
from flask_restful import Api

import config
from api.views.Hello import Hello

api_bp = Blueprint('api', __name__)
api_app = Api(api_bp)

from api import routes
