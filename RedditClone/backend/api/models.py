from datetime import datetime
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

ma = Marshmallow()
db = SQLAlchemy()


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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def email_or_name_exists(email=None, name=None):
        return bool(User.query.filter((User.email == email) | (User.username == name)).first())


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)


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



