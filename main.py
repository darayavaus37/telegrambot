import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from handlers.other import other_router
from handlers.start import start_kb
import random
from handlers import (myinfo,random,start,reviews_dialog)

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()



async def main():
    # запуск бота
    
    dp.include_router(start_kb)
    dp.include_router(other_router)
    dp.include_router(reviews_dialog.review_router)



    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())










