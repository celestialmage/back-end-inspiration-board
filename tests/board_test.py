from app.models.board import Board
from app.db import db
import pytest

@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_no_saved_cards(client):
    # Act
    # Assert