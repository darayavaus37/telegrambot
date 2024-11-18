from aiogram import Router, F, types
from aiogram.filters import Command  
from aiogram.fsm.context import FSMContext

start_kb = Router()

@start_kb.message(Command("start"))
async def start(message: types.Message):
    msg = message.from_user
    name = msg.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="инстаграм курсов",
                    url="https://www.instagram.com/geeks_edu?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
                ),
                types.InlineKeyboardButton(
                    text="инстаграм друга",
                    url="https://www.instagram.com/_ladyrasta?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
                )
            ]
        ]
    )
    await message.answer(f"привет {name}", reply_markup=kb)
