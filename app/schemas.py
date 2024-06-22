from pydantic import BaseModel


class GameBase(BaseModel):
	# id: str ?? treba li
	name: str
	price: float
	platform: str
	genre: str
	description: str
	image_url: str


class GameModel(GameBase):
	id: int
	
	class Config:
		orm_mode = True