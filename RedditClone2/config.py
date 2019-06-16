from praw import Reddit


class Config(object):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True


client_id = '2rKwGPjm5hKxyQ'
client_secret = 'H-5cRKdTYWwhwXfnSZfKz-Rl62Q'
redirect_uri = 'http://127.0.0.1:5000/' # TODO: CHANGE ip to angulars IP
user_agent = 'redditclone'


def get_reddit(refresh_token=None):
    if refresh_token is None or refresh_token is '':
        return Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    return Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, refresh_token=refresh_token)
