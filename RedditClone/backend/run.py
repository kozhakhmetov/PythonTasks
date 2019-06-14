from flask import Flask

from api.models import db
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api import api_bp
from flask_jwt_extended import JWTManager
from api import models
from flask_script import Manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_bp, url_prefix='/api')
    jwt = JWTManager(app)
    with app.app_context():
        db.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return models.RevokedTokenModel.is_jti_blacklisted(jti)

    return app


if __name__ == "__main__":
    app = create_app()


