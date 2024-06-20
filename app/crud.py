from sqlalchemy.orm import Session
from .models import Game as GameModel
from .schemas import GameBase


def get_games(db: Session):
	"""
	Get all games from the database
	
	Args:
		db (Session): SQLAlchemy session
		
	Returns:
		list[Game]: List of games
	"""
	games = db.query(GameModel).all()
	return games


def create_game_crud(db: Session, game: GameBase):
	"""
	Create a new game in the database
	
	Args:
		db (Session): SQLAlchemy session
		game (Game): Game schema
		
	Returns:
		Game: Created game
	"""
	existing_game = db.query(GameModel).filter(GameModel.name == game.name).first()
	if existing_game is not None:
		return None
	
	
	new_game = GameModel(
		name=game.name,
		price=game.price,
		platform=game.platform,
		genre=game.genre,
		description=game.description
	)
	
	db.add(new_game)
	db.commit()
	db.refresh(new_game)
	return GameModel(
		id=new_game.id,
		name=new_game.name,
		price=new_game.price,
		platform=new_game.platform,
		genre=new_game.genre,
		description=new_game.description
	)