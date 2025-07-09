from flask import Blueprint, Response, abort, make_response, request, jsonify
from app.models.board import Board
from app.models.card import Card
from ..db import db
from .route_utils import validate_model, create_model

bp = Blueprint('cards', __name__, url_prefix='/cards')

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

