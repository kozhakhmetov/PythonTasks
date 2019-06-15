from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse
from api.models import LikeToPost, ma, LikeToComment, Post


class LikeToPostSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('post_id', 'value')


like_to_posts_schema = LikeToPostSchema(many=True)
# users_schema = UserSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('post_id', help='This field cannot be blank', required=True, type=int)
parser.add_argument('value', help='This field cannot be blank', required=True, type=int)


class LikeToPostView(Resource):
    @jwt_refresh_token_required
    def get(self):
        user_id = str(get_jwt_identity()['user_id'])
        return like_to_posts_schema.dump(LikeToPost.get_liked_posts(user_id))

    @jwt_refresh_token_required
    def post(self):
        data = parser.parse_args()
        if data['value'] > 1 or data['value'] < -1:
            return {'error': 'value must be in range from 1 to -1'}

        user_id = str(get_jwt_identity()['user_id'])
        LikeToPost.delete_like(user_id=user_id, post_id=data['post_id'])

        new_like = LikeToPost(value=data['value'], user_id=user_id, post_id=data['post_id'])
        try:
            new_like.save_to_db()
            Post.put_like(post_id=data['post_id'], value=data['value'])
            return {'message': 'You liked post with {}'.format(data['post_id'])}
        except Exception as e:
            return {'message': 'Something went wrong' + str(e)}, 500








