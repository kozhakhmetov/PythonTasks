import praw
from flask import request, redirect
from flask_restful import Resource
import config


class Authorization(Resource):
    def get(self):
        reddit = praw.Reddit(client_id=config.client_id,
                             client_secret=config.client_secret,
                             redirect_uri=config.redirect_uri,
                             user_agent=config.user_agent)
        return redirect(reddit.auth.url(['identity', 'edit', 'flair', 'history',
                                         'modconfig', 'modflair', 'modlog',
                                         'modposts', 'modwiki',
                                         'mysubreddits', 'privatemessages',
                                         'read', 'report', 'save', 'submit',
                                         'subscribe', 'vote', 'wikiedit', 'wikiread'], '...', 'permanent'))


class Login(Resource):
    def get(self):
        args = request.args
        reddit = praw.Reddit(client_id=config.client_id,
                             client_secret=config.client_secret,
                             redirect_uri=config.redirect_uri,
                             user_agent=config.user_agent)
        return {'Token': reddit.auth.authorize(args['code'])}


