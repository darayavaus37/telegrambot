from aiogram import Bot,Dispatcher,types,Router,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
#...
review_router= Router()

class Review(StatesGroup):
    name = State()
    inst = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra = State()


@review_router.callback_query(F.data=='review')
async def start_review (call:types.CallbackQuery):
    await call.m.answer('what is your name?')
    await state.set_state(Review.name)

@review_router.message(Review.name)
async def process_name(m:types.Message,state:FSMContext):
    if m.text == m.text.title():
         await state.update_data(name=m.text)
         await m.answer('your instagram account?')
         await state.set_state(Review.inst)
    else:
        await m.answer('write with capital letter!')
        await state.set_state(Review.name)

@review_router.message(Review.inst)
async def procces_inst(m:types,Message,state:FSMContext):
    await state.update_data(inst = m.text)
    await m.answer('what is your visit date?')
    await state.set_state(Review.visit_date)

@review_router.message(Review.visit_date)
async def procces_inst(m:types,Message,state:FSMContext):
    kb = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='bad')],
        [types.KeyboardButton(text='good')]
    ])
    await state.update_data(visit_date = m.text)
    await m.answer('rate the food',reply_markup=kb)
    await state.set_state(Review.food_rating)


@review_router.message(Review.food_rating)
async def procces_inst(m:types,Message,state:FSMContext):
    kb = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='bad')],
        [types.KeyboardButton(text='good')]
    ])
    if m.text in('bad','good'):

       await state.update_data(food_rating = m.text)
       await m.answer('rate the clean',reply_markup=kb)
       await state.set_state(Review.cleanliness_rating)


@review_router.message(Review.cleanliness_rating)
async def procces_inst(m:types,Message,state:FSMContext):
    kb = types.ReplyKeyboardRemove()
    if m.text in('bad','good'):
     await state.update_data(inst = m.text)
     await m.answer('extra comments',reply_markup=kb)
     await state.set_state(Review.extra)


@review_router.message(Review.extra)
async def procces_inst(m:types,Message,state:FSMContext):
    await state.update_data(extra = m.text)
    data= await state.get_data()
    await m.answer(f'{data}\nThank you for review!')
    await state.clear()






