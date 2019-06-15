from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse
from api.models import Post
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('body', required=True)
parser.add_argument('title', required=True)


class PostsView(Resource):
    @jwt_refresh_token_required
    def get(self):
        args = request.args
        user_id = get_jwt_identity()['user_id']
        return Post.get_posts_to_user(user_id, args['limit'], args['offset'])

    @jwt_refresh_token_required
    def post(self):
        data = parser.parse_args()
        current_user = get_jwt_identity()
        new_post = Post(author=str(current_user['user_id']), likes=0, body=data['body'],
                        author_username=current_user['username'], title=data['title'])
        try:
            new_post.save_to_db()
            return {'message': 'Post created'}
        except Exception as e:
            return {'message': 'Something went wrong' + str(e)}, 500










