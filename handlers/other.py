import aiogram
from aiogram import Router, Bot, types
from aiogram.filters import Command
import random
other_router = Router()




@other_router.message(Command('myinfo'))
async def userinfo_handler(message: types.Message):
    yourid = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer (f"Ваш id: {yourid}\nВаше имя: {first_name}\nВаш username: {username}")




@other_router.message() 
async def echo_handler(message: types.Message):
    # обработчик всех сообщений
    await message.answer(message.text)