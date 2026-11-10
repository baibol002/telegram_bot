CREATE_MOVIES_TABLE = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        rating INTEGER NOT NULL
    )
"""

INSERT_MOVIE = """
    INSERT INTO movies (title, genre, rating)
    VALUES (?, ?, ?)
"""

SELECT_ALL_MOVIES = """
    SELECT id, title, genre, rating FROM movies
"""
