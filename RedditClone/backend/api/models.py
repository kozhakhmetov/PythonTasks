import datetime
from run import db, app
import datetime as dt
from datetime import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    karma = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    body = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    likes = db.Column(db.Integer, nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    body = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    post = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    likes = db.Column(db.Integer, nullable=False)


class LikeToComment(db.Model):
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True, index=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False, primary_key=True)


class LikeToPost(db.Model):
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True)


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)


class CollectionToPost(db.Model):
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True)



