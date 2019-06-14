from flask import Blueprint
from flask_restful import Api
from api.views.Hell import Hello

api_bp = Blueprint('api', __name__)
api_app = Api(api_bp)

from api import routes, models
