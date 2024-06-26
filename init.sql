CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    description TEXT,
    image_url TEXT
);