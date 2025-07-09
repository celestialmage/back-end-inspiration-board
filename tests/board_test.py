from app.models.board import Board
from app.db import db
import pytest

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_by_board(client, one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Build a habit of going outside daily",
        "owner": "Ellie",
        "cards": []
    }


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board_must_contain_title(client):
    # Act
    response = client.post("/boards", json={
        "owner": "Test owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert db.session.scalars(db.select(Board)).all() == []


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board_must_contain_owner(client):
    # Act
    response = client.post("/boards", json={
        "title": "A Brand New Board"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert db.session.scalars(db.select(Board)).all() == []