from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.db import add_movie, get_all_movies


class AddMovie(StatesGroup):
    title = State()
    genre = State()
    rating = State()


router_fsm = Router()


@router_fsm.message(Command('movies'))
async def movies_handler(message: Message):
    movies = get_all_movies()
    if not movies:
        await message.answer('В базе пока нет фильмов. Добавь первый через /form')
        return

    text = 'Список фильмов:\n\n'
    for movie_id, title, genre, rating in movies:
        text += f'{movie_id}. {title} — {genre}, оценка: {rating}/10\n'
    await message.answer(text)


@router_fsm.message(Command('form'))
async def start_form(message: Message, state: FSMContext):
    await message.answer('Напиши название фильма')
    await state.set_state(AddMovie.title)


@router_fsm.message(AddMovie.title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer('Какой жанр у фильма?')
    await state.set_state(AddMovie.genre)


@router_fsm.message(AddMovie.genre)
async def get_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer('Поставь оценку от 1 до 10')
    await state.set_state(AddMovie.rating)


@router_fsm.message(AddMovie.rating)
async def get_rating(message: Message, state: FSMContext):
    if not message.text or not message.text.isdigit() or not 1 <= int(message.text) <= 10:
        await message.answer('Оценка должна быть числом от 1 до 10!')
        return

    await state.update_data(rating=int(message.text))
    data = await state.get_data()

    add_movie(data['title'], data['genre'], data['rating'])

    await message.answer(
        f'Фильм добавлен!\n'
        f'Название: {data["title"]}\n'
        f'Жанр: {data["genre"]}\n'
        f'Оценка: {data["rating"]}/10'
    )
    await state.clear()
