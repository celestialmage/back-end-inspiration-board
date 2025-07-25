from flask import Flask
from .db import db, migrate
from flask_cors import CORS
import os
# Import models, blueprints, and anything else needed to set up the app or database
from .models.board import Board
from .models.card import Card
from .routes.board_routes import bp as boards_bp
from .routes.card_routes import bp as cards_bp


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints 
    app.register_blueprint(boards_bp)
    app.register_blueprint(cards_bp)


    CORS(app)
    return app
