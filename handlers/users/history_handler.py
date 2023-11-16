from aiogram import types

from loader import dp, bot


@dp.message_handler(text='🗒 История моих покупок')
async def top_products(message: types.Message):
    await message.answer('Эта функция еще не доступно!')
