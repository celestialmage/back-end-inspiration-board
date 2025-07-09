from app.models.card import Card
from app.db import db
import pytest

# @pytest.mark.skip(reason="No way to test this feature yet")
# def test_get_cards_no_saved_cards(client):
#     # Act
#     # Assert

@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_board_not_found(client):
    # Act
    response = client.get("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}