from sqlalchemy.orm import Session
from .models import Game as GameModel
from .schemas import GameBase


def get_games_crud(db: Session):
	return db.query(GameModel).all()


def create_game_crud(db: Session, game: GameBase):
	existing_games = db.query(GameModel).filter(GameModel.name == game.name).first()
	if existing_games is not None:
		return None
	
	new_game = GameModel(**game.dict())
	db.add(new_game)
	db.commit()
	db.refresh(new_game)
	return new_game


def delete_game_crud(db: Session, game_id: int):
	game = db.query(GameModel).filter(GameModel.id == game_id).first()
	if game is None:
		return None
	
	db.delete(game)
	db.commit()
	return True