from api.models import User, RevokedTokenModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)
parser.add_argument('email', required=False)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if User.email_or_name_exists(name=data['username'], email=data['email']):
            return {'message': 'User already exists'}

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        try:
            new_user.save_to_db()
            refresh_token = create_refresh_token(identity=new_user.id)
            return {
                'message': 'User {} was created'.format(data['username']),
                'token': refresh_token
            }
        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if current_user.check_password(data['password']):
            refresh_token = create_refresh_token(identity=current_user.id)
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked' + str(jti)}
        except Exception as e:
            return {'message': 'Something went wrong'}, 500
