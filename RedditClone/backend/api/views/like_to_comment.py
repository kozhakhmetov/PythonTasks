from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse
from api.models import ma, LikeToComment, Comment


class LikeToCommentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('comment_id', 'value')


like_to_comments_schema = LikeToCommentSchema(many=True)

parser_like = reqparse.RequestParser()
parser_like.add_argument('comment_id', help='This field cannot be blank', required=True, type=int)
parser_like.add_argument('value', help='This field cannot be blank', required=True, type=int)


class LikeToCommentView(Resource):
    @jwt_refresh_token_required
    def get(self):
        user_id = get_jwt_identity()
        return like_to_comments_schema.dump(LikeToComment.get_liked_comments(user_id))

    @jwt_refresh_token_required
    def post(self):
        data = parser_like.parse_args()
        if data['value'] > 1 or data['value'] < -1:
            return {'error': 'value must be in range from 1 to -1'}

        user_id = get_jwt_identity()
        LikeToComment.delete_like(user_id=user_id, comment_id=data['comment_id'])
        new_like = LikeToComment(value=data['value'], user_id=user_id, comment_id=data['comment_id'])
        try:
            new_like.save_to_db()
            Comment.put_like(comment_id=data['comment_id'], value=data['value'])
            return {'message': 'You liked comment with {}'.format(data['comment_id'])}
        except Exception as e:
            return {'message': 'Something went wrong'}, 500
