import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

if POSTGRES_URL is None:
	raise RuntimeError("Env POSTGRES_URL is not set")

if POSTGRES_DATABASE is None:
	raise RuntimeError("Env POSTGRES_DATABASE is not set")

if POSTGRES_USER is None:
	raise RuntimeError("Env POSTGRES_USER is not set")

if POSTGRES_PASSWORD is None:
	raise RuntimeError("Env POSTGRES_PASSWORD is not set")

url = URL.create(
	drivername="postgresql",
	username=POSTGRES_USER,
	password=POSTGRES_PASSWORD,
	host="db",
	database=POSTGRES_DATABASE,
	port=5432
)

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)