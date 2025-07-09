import pytest
from app.__init__ import create_app # recheck the route
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.card import Card
from app.models.board import Board

load_dotenv()

@pytest.fixture
def app():
    # create the app with a test configuration
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

# **********************************************
#  Example Fixtures From Task API TO BE REVISED
# **********************************************
# This fixture gets called in every test that
# references "one_card"
# This fixture creates a card and saves it in the database
@pytest.fixture
def one_card(app):
    new_card = Card(
                    message="Go on my daily walk 🏞", 
                    likes_count=1
                    )
    db.session.add(new_card)
    db.session.commit()


# This fixture gets called in every test that
# references "three_cards"
# This fixture creates three cards and saves
# them in the database
@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(message="Water the garden 🌷", 
            likes_count=1),
        Card(message="Answer forgotten email 📧", 
            likes_count=0),
        Card(message="Pay my outstanding tickets 😭", 
            likes_count=2)
    ])
    db.session.commit()


# This fixture gets called in every test that
# references "liked_card"
# This fixture creates a card with a
@pytest.fixture
def liked_card(app):
    new_card = Card(message="Explore Seattle 🏞", 
                    likes_count=0)
    db.session.add(new_card)
    db.session.commit()


# This fixture gets called in every test that
# references "one_board"
# This fixture creates a board and saves it in the database
@pytest.fixture
def one_board(app):
    new_board = Board(title="Build a habit of going outside daily",
                    owner= "Ellie",
                    )
    db.session.add(new_board)
    db.session.commit()


# This fixture gets called in every test that
# references "one_card_belongs_to_one_board"
# This fixture creates a card and a board
# It associates the board and card, so that the
# board has this card, and the card belongs to one board
@pytest.fixture
def one_card_belongs_to_one_board(app, one_board, one_card):
    card_query = db.select(Card).where(Card.id == 1)
    board_query = db.select(Board).where(Board.id == 1)
    card = db.session.scalar(card_query)
    board = db.session.scalar(board_query)
    board.cards.append(card)
    db.session.commit()