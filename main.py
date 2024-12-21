from aiogram import executor
from config import *
import texts
from keyboards import *
from admin import *
from crud_functions import *

initiate_db()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"{message.from_user.username}, добро пожаловать в наш магазин! "+texts.starts, reply_markup = start_kb)

@dp.callback_query_handler(text = "О нас")
async def price_message(call):
    await call.message.answer(texts.about, reply_markup = start_kb)
    await call.answer()

@dp.callback_query_handler(text ="Купить")
async def about_message(call):
    for product in get_all_products():
        await call.message.answer(f"{product[1]}\n{product[2]}\nЦена: {product[3]} руб")
        with open(f'image\{product[1]}.jpg', 'rb') as img:
            await call.message.answer_photo(img)

    await call.message.answer("Купить: ", reply_markup = price_kb)

@dp.callback_query_handler(text = "Buy")
async def other_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(text = "Other")
async def other_message(call):
    await call.message.answer(texts.other_work)
    await call.answer()

if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)

