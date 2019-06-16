import praw
from flask import Flask

import config
from api import api_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

