from flask import Blueprint, Response, abort, make_response, request, jsonify
from app.models.board import Board
from app.models.card import Card
from ..db import db
from .route_utils import validate_model, create_model

bp = Blueprint("boards", __name__, url_prefix="/boards")

# POST/boards request Creating a new board
@bp.post("")
def create_board():
    request_body = request.get_json()
    model_dict, status = create_model(Board, request_body)
    return model_dict, status


# GET/boards request reading all boards
@bp.get("")
def get_all_boards():

    query = db.select(Board)

    sort_param = request.args.get("sort")
    if sort_param == "asc":
        query = query.order_by(Board.title.asc())
    elif sort_param == "desc":
        query = query.order_by(Board.title.desc())
    else:
        query = query.order_by(Board.board_id)

    boards = db.session.scalars(query)
    
    boards_response = []
    for board in boards:
        boards_response.append(board.to_dict())

    return boards_response


# GET/<id>/boards reading all cards of a board <id>
@bp.get("/<board_id>/cards")
def read_cards_for_board(board_id):
    board = validate_model(Board, board_id)

    cards_response = []
    for card in board.cards:
        card_dict = {
            "card_id": card.card_id,
            "message": card.message,
            "likes_count": card.likes_count,
            "board_id": board.board_id,
        }
        cards_response.append(card_dict)

    response_body = {
        "id": board.board_id,
        "title": board.title,
        "owner": board.owner,
        "cards": cards_response  
    }

    return jsonify(response_body), 200