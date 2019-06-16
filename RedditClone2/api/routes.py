from api import api_app
from api.views.Hello import Hello
from api.views.authorization import Authorization, Login
from api.views.like import LikeToComment, LikeToPost
from api.views.post import Posts, Post, SubredditPosts
from api.views.user import UserMe

api_app.add_resource(Hello, '/hello/')
api_app.add_resource(Authorization, '/auth/')
api_app.add_resource(Login, '/login/')
api_app.add_resource(UserMe, '/me/')
api_app.add_resource(Posts, '/front/posts/hot/')
api_app.add_resource(SubredditPosts, '/subreddit/posts/hot/<string:subreddit>/')
api_app.add_resource(Post, '/post/<string:post_id>/')
api_app.add_resource(LikeToPost, '/vote/post/<string:post_id>/')
api_app.add_resource(LikeToComment, '/vote/comment/<string:comment_id>/')