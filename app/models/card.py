from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .board import Board

class Card(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey('board.id'))
    board: Mapped['Board'] = relationship(back_populates='cards')

    def to_dict(self):

        card_dict = {
            'id': self.id,
            'message': self.message,
            'likes_count': self.likes_count,
            'board_id': self.board_id
        }

        return card_dict
    
    @classmethod
    def from_dict(cls, card_data):

        card_data['likes_count'] = 0

        new_card = Card(message=card_data['message'],
                        likes_count=card_data['likes_count'],
                        board_id=card_data['board_id'])
        
        return new_card