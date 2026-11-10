from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Addproduct(StatesGroup):
    name_product = State()
    alcohol = State()
    status = State()
    price = State()

router_add_product = Router()

@router_add_product.message(Command('add_product'))
async def start_add_product(message: Message, state: FSMContext):
    await message.answer('Напиши название напитка')
    await state.set_state(Addproduct.name_product)


@router_add_product.message(Addproduct.name_product)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name_product=message.text)
    await message.answer('Он алкогольный или нет?')
    await state.set_state(Addproduct.alcohol)


@router_add_product.message(Addproduct.alcohol)
async def get_alcohol(message: Message, state: FSMContext):
    await state.update_data(alcohol=message.text)
    await message.answer('Он на складе или в пути?')
    await state.set_state(Addproduct.status)


@router_add_product.message(Addproduct.status)
async def get_status(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.answer('Напиши стоимость')
    await state.set_state(Addproduct.price)


@router_add_product.message(Addproduct.price)
async def get_price(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Стоимость должна быть числом!')
        return
    data = await state.get_data()
    await message.answer(f'Напиток: {data["name_product"]}\nАлкогольный: {data["alcohol"]}\nСтатус: {data["status"]}\nСтоимость: {message.text} сом')
    await state.clear()
