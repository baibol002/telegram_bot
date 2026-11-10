import sqlite3

from database import queries

DB_NAME = 'movies.db'


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(queries.CREATE_MOVIES_TABLE)


def add_movie(title, genre, rating):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(queries.INSERT_MOVIE, (title, genre, rating))


def get_all_movies():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute(queries.SELECT_ALL_MOVIES).fetchall()
