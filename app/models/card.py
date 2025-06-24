from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Card(db.Model):

    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey('board.id'))
    board: Mapped['Board'] = relationship(back_populates='board')

    def to_dict(self):

        card_dict = {
            'card_id': self.card_id,
            'message': self.message,
            'likes_count': self.likes_count,
            'board_id': self.board_id
        }

        return card_dict
    
    @classmethod
    def from_dict(cls, card_data):

        new_card = Card(card_id=card_data['card_id'],
                        message=card_data['message'],
                        likes_count=card_data['likes_count'],
                        board_id=card_data['board_id'])
        
        return new_card