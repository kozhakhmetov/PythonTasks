from api import api_app
from api.views.Hell import Hello


api_app.add_resource(Hello, '/hello/')