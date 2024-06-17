from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# TEMP, TESTING DB
class GameBase(BaseModel):
    id: int
    name: str
    price: float
    platform: str
    genre: str
    description: str


@app.get("/")
def read_root():
    return {"Hello": "World"}
