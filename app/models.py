from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	...


class Game(Base):
	__tablename__ = 'games'
	
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	price: Mapped[float]
	platform: Mapped[str]
	genre: Mapped[str]
	description: Mapped[str]
	image_url: Mapped[str]
	
	def __repr__(self):
		return f"{self.name} {self.price}$"