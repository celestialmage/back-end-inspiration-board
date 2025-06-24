from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
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
            ''
        }