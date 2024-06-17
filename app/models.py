from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Game(DeclarativeBase):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    platform: Mapped[str]
    genre: Mapped[str]
    description: Mapped[str]

    def __repr__(self):
        return f"{self.name} {self.price}$"
