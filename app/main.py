import time

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles  # For serving static files
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from starlette import status

from app.database import SessionLocal, engine
from app.models import Game, Base
from app.schemas import GameBase, GameModel
from app.crud import get_games_crud, create_game_crud, delete_game_crud

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
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


@app.get("/", response_class=FileResponse)
def read_root():
	return "app/static/index.html"


@app.get("/games")
def get_games(db: Session = Depends(get_db), response_model=list[GameModel]):
	return get_games_crud(db)


@app.get("/games/{game_id}", response_model=GameModel)
def get_game(game_id: int, db: Session = Depends(get_db)):
	game = db.query(Game).filter(Game.id == game_id).first()
	if game is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
	
	return game


@app.post("/create", response_model=GameModel)
def create_game(game: GameBase, db: Session = Depends(get_db)):
	print("Method create called")
	new_game = create_game_crud(db, game)
	if new_game is None:
		raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Game already exists")
	
	return new_game


@app.put("/games/{game_id}", response_model=GameModel)
def update_game(game_id: int, game: GameBase, db: Session = Depends(get_db)):
	existing_game = db.query(Game).filter(Game.id == game_id).first()
	if existing_game is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
	
	for key, value in game.dict().items():
		setattr(existing_game, key, value)
	
	db.commit()
	db.refresh(existing_game)
	
	return existing_game


@app.delete("/games/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
	game_deleted = delete_game_crud(db, game_id)
	if game_deleted is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
	
	return {"message": "Game deleted"}