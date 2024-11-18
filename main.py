import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import random

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f'Привет, {name}!Ведите одну из команд : myinfo; random; start;'
    await message.answer(msg)


@dp.message(Command('myinfo'))
async def userinfo_handler(message: types.Message):
    yourid = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer (f"Ваш id: {yourid}\nВаше имя: {first_name}\nВаш username: {username}")


thenames = ["Иван", "Анна", "Максим", "Елена", "Дмитрий", "Ольга", "Алексей", "Мария", "Петр"]
@dp.message(Command('random'))
async def randomchoise_handler(message: types.Message):
    random_name = random.choice(thenames) 
    await bot.send_message(message.chat.id, f"Случайное имя: {random_name}")



@dp.message() 
async def echo_handler(message: types.Message):
    # обработчик всех сообщений
    await message.answer(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())








