from api import api_app
from api.views.Hell import Hello
from api.views.auth import UserRegistration, UserLogin, UserLogoutRefresh
from api.views.like_to_comment import LikeToCommentView
from api.views.like_to_post import LikeToPostView
from api.views.post import PostsView
from api.views.user import UsersView, UserView


api_app.add_resource(Hello, '/hello/')
api_app.add_resource(UserRegistration, '/auth/user/')
api_app.add_resource(UserLogin, '/auth/login/')
api_app.add_resource(UserLogoutRefresh, '/auth/logout/')
api_app.add_resource(UsersView, '/users/')
api_app.add_resource(UserView, '/user/<int:pk>/')
api_app.add_resource(PostsView, '/posts/')
api_app.add_resource(LikeToPostView, '/like_to_post/')
api_app.add_resource(LikeToCommentView, '/like_to_comment/')
