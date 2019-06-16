import config
from flask_restful import Resource, reqparse
from api.serilizers import to_json_post, to_json_comment

parser = reqparse.RequestParser()
parser.add_argument('Authorization', required=True, location='headers')


class Posts(Resource):
    def get(self):
        token = ''
        data = parser.parse_args()
        if 'Authorization' in data:
            token = parser.parse_args()['Authorization'].split()
        reddit = config.get_reddit(token)
        front = reddit.front.hot(limit=10)
        return {'posts': [to_json_post(post) for post in front]}


class Post(Resource):
    def get(self, post_id):
        token = ''
        data = parser.parse_args()
        if 'Authorization' in data:
            token = data['Authorization'].split()
        reddit = config.get_reddit(token)
        post = reddit.submission(post_id)
        comments = post.comments
        return {'post': to_json_post(post, show_body=True),
                'comments': [to_json_comment(comment_) for comment_ in comments]}


class SubredditPosts(Resource):
    def get(self, subreddit):
        token = ''
        data = parser.parse_args()
        if 'Authorization' in data:
            token = data['Authorization'].split()
        reddit = config.get_reddit(token)
        front = reddit.subreddit(subreddit).hot(limit=10)
        return {'posts': [to_json_post(post) for post in front]}
