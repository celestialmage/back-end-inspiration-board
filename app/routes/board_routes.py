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


# POST/boards/<board_id>/cards
@bp.post("/<board_id>/cards")
def create_card(board_id):

    validate_model(Board, board_id)

    request_body = request.get_json()

    request_body['board_id'] = board_id

    if len(request_body['message']) > 40:
        response = { 'message': 'Message must be shorter than 40 charaters' }
        abort(make_response(response, 400))

    model_dict, status = create_model(Card, request_body)
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
        query = query.order_by(Board.id)

    boards = db.session.scalars(query)
    
    boards_response = []
    for board in boards:
        boards_response.append(board.to_dict())

    return boards_response


# GET/<id>/boards reading all cards of a board <id>
@bp.get("/<id>/cards")
def read_cards_for_board(id):
    board = validate_model(Board, id)

    cards_response = []
    for card in board.cards:
        cards_response.append(card.to_dict())

    return cards_response, 200