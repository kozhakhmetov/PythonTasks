from flask_jwt_extended import jwt_refresh_token_required
from flask_restful import Resource
from api.models import User, ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('email', 'username', 'karma', 'id')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UsersView(Resource):
    @jwt_refresh_token_required
    def get(self):
        return users_schema.dump(User.query.all())


class UserView(Resource):
    @jwt_refresh_token_required
    def get(self, pk):
        user = User.query.get(pk)
        if not user:
            return {'error': 'User with such id doesn\'t exist'}, 404
        return user_schema.dump(user)

