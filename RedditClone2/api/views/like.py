import config
import praw
praw.models.Submission
from flask import request, redirect
from flask_restful import Resource, reqparse
from praw.models.reddit import comment
from api.serilizers import to_json_user, to_json_post, to_json_comment

parser = reqparse.RequestParser()
parser.add_argument('value', required=True, type=int)
parser.add_argument('Authorization', required=True, location='headers')


class LikeToPost(Resource):
    def post(self, post_id):
        token = parser.parse_args()['Authorization'].split()[1]
        value = parser.parse_args()['value']
        reddit = config.get_reddit(token)

        post = reddit.submission(post_id)
        try:
            if value > 0:
                post.upvote()
            elif value < 0:
                post.downvote()
            else:
                post.clear_vote()
            return {'message' : 'you voted'}
        except Exception as e:
            return {'error': str(e)}


class LikeToComment(Resource):
    def post(self, comment_id):
        token = parser.parse_args()['Authorization'].split()[1]
        value = parser.parse_args()['value']
        reddit = praw.Reddit(client_id=config.client_id,
                             client_secret=config.client_secret,
                             refresh_token=token,
                             user_agent=config.user_agent)
        comment = reddit.comment(comment_id)
        try:
            if value > 0:
                comment.upvote()
            elif value < 0:
                comment.downvote()
            else:
                comment.clear_vote()
        except Exception as e:
            return {'error': str(e)}