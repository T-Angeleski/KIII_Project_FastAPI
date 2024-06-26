import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

# POSTGRES_URL = os.getenv("POSTGRES_URL")
print("Getting ENV variables")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)

# url = URL.create(
# 	drivername="postgresql",
# 	username=POSTGRES_USER,
# 	password=POSTGRES_PASSWORD,
# 	host=POSTGRES_HOST,
# 	database=POSTGRES_DATABASE,
# 	port=POSTGRES_PORT
# )
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Testing connection
try:
	with engine.connect() as connection:
		print("Connection to database successful!")
		print(f"URL: {SQLALCHEMY_DATABASE_URL}")
except Exception as e:
	print(f"Error connecting: {str(e)}")
	print(f"URL: {SQLALCHEMY_DATABASE_URL}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)