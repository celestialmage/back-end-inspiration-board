from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from ..db import db

class Board(db.Model):
    board_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list['Card']] = relationship(back_populates='board')

    