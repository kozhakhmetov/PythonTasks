import praw
from flask import request, redirect
from flask_restful import Resource, reqparse
from config import get_reddit
from api.serilizers import to_json_user

parser = reqparse.RequestParser()
parser.add_argument('Authorization', required=True, location='headers')


class UserMe(Resource):
    def get(self):
        token = parser.parse_args()['Authorization'].split()[1]

        reddit = get_reddit(token)

        redditor = reddit.user.me()
        print(reddit.auth.scopes())

        return to_json_user(redditor)

