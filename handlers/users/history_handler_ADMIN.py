from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, db
from markups.Inlinekeyboard.history_markup import markup_history


@dp.message_handler(text='🗒 История заказов[ADMIN]')
async def top_products(message: types.Message):
    await message.answer('Выберите:', reply_markup=markup_history)


@dp.callback_query_handler(text='waiting')
async def waiting(callback: types.CallbackQuery):
    await callback.message.delete()
    dates = db.execute(f'select o.date from oformlenie o join registration r on r.id = o.user_id where r.user_id = {callback.from_user.id} and check_zakaz == False', fetchall=True)
    markup = InlineKeyboardMarkup()
    for i in dates:
        for j in i:
            markup.insert(InlineKeyboardButton(text=j, callback_data=j))
    await callback.message.answer('Выберите дату', reply_markup=markup)
