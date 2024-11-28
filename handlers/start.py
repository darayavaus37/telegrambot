from aiogram import Bot,Dispatcher,types,Router,F
from aiogram.filters import Command
start_router= Router()
kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='review',callback_data = 'review' )]
])
@start_router.message(Command('start'))
async def start(message:types.Message):
    await message.answer(f'hello {message.from_user.first_name}',reply_markup=kb)
@start_router.callback_query(F.data == 'hi')
async def hi(call: types.CallbackQuery):
    await call.message.answer('HIIIIIIIIII')

















# from aiogram import Router, F, types
# from aiogram.filters import Command  
# from aiogram.fsm.context import FSMContext

# start_kb = Router()


# kb = types.InlineKeyboardMarkup(inline_keyboard=[ 
#     [types.InlineKeyboardButton(text='review' , 
# callback_data = 'review')]
# ])


# @start_kb.message(Command("start"))
# async def start(message: types.Message):
#     msg = message.from_user
#     name = msg.first_name
#     kb = types.InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 types.InlineKeyboardButton(
#                     text="инстаграм курсов",
#                     url="https://www.instagram.com/geeks_edu?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
#                 ),
#                 types.InlineKeyboardButton(
#                     text="инстаграм друга",
#                     url="https://www.instagram.com/_ladyrasta?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
#                 )
#             ]
#         ]
#     )
#     await message.answer(f"привет {name}", reply_markup=kb)
