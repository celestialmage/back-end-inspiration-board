from flask import Blueprint, Response, abort, make_response, request, jsonify
from app.models.board import Board
from app.models.card import Card
from ..db import db
from .route_utils import validate_model, create_model

bp = Blueprint('cards', __name__, url_prefix='/cards')

@bp.post('')
def create_card():
    board_id = request.args.get('board_id')

    request_body = request.get_json()

    request_body['board_id'] = board_id

    if len(request_body['message']) > 40:
        response = { 'message': 'Message must be shorter than 40 charaters' }
        abort(make_response(response, 400))

    model_dict, status = create_model(Card, request_body)
    return model_dict, status

@bp.get('/')
def get_all_cards():

    board_id = request.args.get('board_id')

    query = db.select(Card).where(Card.board_id == board_id)

    cards = db.session.scalars(query)

    cards_response = []

    for card in cards:
        cards_response.append(card.to_dict())

    return cards_response

@bp.delete('/<card_id>')
def remove_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@bp.patch('/<card_id>/like')
def like_card(card_id):
    card = validate_model(Card, card_id)

    card.likes_count += 1

    db.session.commit()

    return Response(status=204, mimetype='application/json')