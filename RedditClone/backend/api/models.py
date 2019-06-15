from datetime import datetime
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
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

    @classmethod
    def delete_user(cls, user_id):
        cls.query.filter_by(id=user_id).delete()
        db.session.commit()

    @staticmethod
    def email_or_name_exists(email=None, name=None):
        return bool(User.query.filter((User.email == email) | (User.username == name)).first())

    @classmethod
    def karma_update(cls, user_id, value):
        cls.query.filter_by(id=user_id).first().karma += value
        db.session.commit()


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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    author_username = db.Column(db.String, nullable=False, index=True)
    body = db.Column(db.String(10000), nullable=False)
    title = db.Column(db.String(1000), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def put_like(cls, post_id, value):
        cls.query.filter_by(id=post_id).first().likes += value
        db.session.commit()

    @classmethod
    def get_posts_to_user(cls, user_id, limit, offset):
        posts = db.engine.execute('SELECT * FROM post left join '
                                  '(SELECT * FROM like_to_post WHERE user_id={}) '
                                  'AS post2 on post.id = post2.post_id LIMIT {} OFFSET {};'
                                  .format(user_id, limit, offset))

        def to_json(x):
            return {
                'id': x.id,
                'author_id': x.author,
                'title': x.title,
                'like_by_user': x.value if x.value is not None else 0,
                'author_username': x.author_username,
                'body': x.body,
                'date_created': str(x.date_created)
            }
        return [to_json(x) for x in posts]


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    author_username = db.Column(db.String, nullable=False, index=True)

    body = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    post = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def put_like(cls, comment_id, value):
        cls.query.filter_by(id=comment_id).first().likes += value
        db.session.commit()


class LikeToComment(db.Model):
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True, index=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False, primary_key=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_liked_comments(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def delete_like(cls, comment_id, user_id):
        query = cls.query.filter_by(comment_id=comment_id, user_id=user_id)
        if query.first():
            Comment.put_like(comment_id=comment_id, value=-query.first().value)
        query.delete()
        db.session.commit()


class LikeToPost(db.Model):
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_liked_posts(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def delete_like(cls, post_id, user_id):
        query = cls.query.filter_by(post_id=post_id, user_id=user_id)
        if query.first():
            Post.put_like(post_id=post_id, value=-query.first().value)
        query.delete()
        db.session.commit()


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CollectionToPost(db.Model):
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
