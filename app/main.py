import time

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.database import SessionLocal, engine
from app.models import Base, Game
from app.schemas import GameBase
from app.crud import get_games, create_game_crud

app = FastAPI()

# Ensures that the database is created before the application starts
for i in range(3):
	try:
		Base.metadata.create_all(bind=engine)
		break
	except OperationalError:
		time.sleep(i + 5)


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.get("/games")
def get_games(db: Session = Depends(get_db)):
	return get_games(db)


@app.post("/create", response_model=GameBase)
def create_game(game: GameBase, db: Session = Depends(get_db)):
	new_game = create_game_crud(db, game)
	
	if not new_game:
		return {"message": "Game could not be created"}
	
	return new_game