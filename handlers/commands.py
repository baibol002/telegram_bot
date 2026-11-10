import random
from datetime import datetime

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot

router_commands = Router()

jokes = [
    'Программист — это машина для превращения кофе в код.',
    'Почему программисты путают Хэллоуин и Рождество? Потому что 31 OCT = 25 DEC.',
    '— Сколько программистов нужно, чтобы вкрутить лампочку? — Ни одного, это проблема железа.',
    'Работает — не трогай. Не работает — тоже не трогай, вдруг заработает.',
    'Лучший способ ускорить компьютер — бросить его из окна повыше.',
]

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Привет мир!')

    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привет! {message.from_user.full_name} \nТвой телеграм ID > {message.from_user.id}')


@router_commands.message(F.text == 'привет')
async def hello_handler(message: Message):
    await message.answer('Салам')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM5auCySPyaBYsHzBJnxxDp79pfm1sAAqirAAKFa_lIF38CcJWB3Wg9BA')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM1auCx0ITQ88ljCxCaBsYQuKdB2vEAAuMAA1eEbA_LD3f9g8IMvD0E')



@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo = FSInputFile('media/image.png')
    await message.answer_photo(photo=photo)


@router_commands.message(Command('time'))
async def time_handler(message: Message):
    now = datetime.now().strftime('%d.%m.%Y %H:%M')
    await message.answer(f'Сейчас: {now}')


@router_commands.message(Command('random'))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f'Твоё случайное число: {number}')


@router_commands.message(Command('joke'))
async def joke_handler(message: Message):
    joke = random.choice(jokes)
    await message.answer(joke)
