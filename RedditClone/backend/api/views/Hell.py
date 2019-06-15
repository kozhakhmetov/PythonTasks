from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource


class Hello(Resource):
    @jwt_refresh_token_required
    def get(self):
        current_user = get_jwt_identity()
        return {"message": "Hello, World!" + str(current_user)}
