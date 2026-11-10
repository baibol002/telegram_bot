import asyncio
import logging

from aiogram.types import BotCommand

from config import bot, dp
from database.db import init_db
from handlers import commands, echo, fsm_add_product, fsm


dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm_add_product.router_add_product)
dp.include_router(router=fsm.router_fsm)
dp.include_router(router=echo.router_echo)


bot_commands = [
    BotCommand(command='start', description='Запустить бота'),
    BotCommand(command='time', description='Текущая дата и время'),
    BotCommand(command='random', description='Случайное число от 1 до 100'),
    BotCommand(command='joke', description='Случайная шутка'),
    BotCommand(command='sticker', description='Прислать стикеры'),
    BotCommand(command='mem', description='Прислать мем'),
    BotCommand(command='form', description='Добавить фильм'),
    BotCommand(command='movies', description='Список фильмов из базы'),
    BotCommand(command='add_product', description='Добавить напиток'),
]


async def main():
    init_db()
    await bot.set_my_commands(bot_commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
