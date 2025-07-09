from app.models.card import Card
from app.db import db
import pytest


# Test deleting a card successfully
# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_card(client, one_card_belongs_to_one_board):
    # Delete the card
    response = client.delete('/cards/1')
    assert response.status_code == 204

    # After deletion, check cards in the board, card 1 should be gone
    get_response = client.get('/boards/1/cards')
    cards = get_response.get_json()
    assert all(card['id'] != 1 for card in cards)


# Test liking a card increments likes_count
# @pytest.mark.skip(reason="No way to test this feature yet")
def test_like_card(client, one_card_belongs_to_one_board):
    # Like the card
    response = client.patch('/cards/1/like')
    assert response.status_code == 204

    # Get all cards for the board, and verify likes_count incremented
    get_response = client.get('/boards/1/cards')
    cards = get_response.get_json()

    # There should be exactly one card with id=1
    card = next(card for card in cards if card['id'] == 1)

    # Assuming fixture card has likes_count=1, it should now be 2
    assert card['likes_count'] == 2
