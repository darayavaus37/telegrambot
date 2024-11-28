from aiogram import Bot,Dispatcher
from dotenv import dotenv_values
from datbase.db import Database
token = dotenv_values('.env')['BOT_TOKEN']
bot=Bot(token=token)
dp = Dispatcher()
db = Database('database/db.sqlite3')
