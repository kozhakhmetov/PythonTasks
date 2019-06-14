from api import api_app
from api.views.Hell import Hello
from api.views.auth import UserRegistration, UserLogin, UserLogoutRefresh


api_app.add_resource(Hello, '/hello/')
api_app.add_resource(UserRegistration, '/auth/registration/')
api_app.add_resource(UserLogin, '/auth/login/')
api_app.add_resource(UserLogoutRefresh, '/auth/logout/')
