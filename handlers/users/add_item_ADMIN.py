from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import ADMINS
from loader import dp
from markups.defaultkeyboard.menu_markup import menu_markup_def_admin, menu_markup_def
from query_data.config import insert_item, get_kategory
from states.add_item import Item


@dp.message_handler(text='➕ Добавить товар[ADMIN]')
async def add_item(message: types.Message):
    kategory_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in get_kategory():
        button = KeyboardButton(text=i)
        kategory_markup.insert(button)
    button_back = KeyboardButton(text='🔚 Главный меню')
    kategory_markup.add(button_back)
    await message.answer("Выберите категорию для продукта или напишите сами", reply_markup=kategory_markup)
    await Item.kategory.set()


@dp.message_handler(state=Item.kategory)
async def kategory_def(message: types.Message, state: FSMContext):
    if message.text == '🔚 Главный меню':
        await state.finish()
        await message.delete()
        if str(message.from_user.id) in ADMINS:
            await message.answer('Главный меню', reply_markup=menu_markup_def_admin)
        else:
            await message.answer('Главный меню', reply_markup=menu_markup_def)
    else:
        kategory = message.text
        await state.update_data(
            {"kategory": kategory}
        )
        await message.answer("Теперь название товара")
        await Item.next()


@dp.message_handler(state=Item.name)
async def name_def(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Информация о товаре")
    await Item.next()


@dp.message_handler(state=Item.info)
async def info_def(message: types.Message, state: FSMContext):
    info = message.text
    await state.update_data(
        {"info": info}
    )
    await message.answer("Сколко стоит этот товар на штуку")
    await Item.next()


@dp.message_handler(state=Item.price)
async def price_def(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(
        {'price': price}
    )
    await message.answer("Количество этого товара в наличии\n[1-1000]")
    await Item.next()


@dp.message_handler(state=Item.count)
async def count_def(message: types.Message, state: FSMContext):
    count = message.text
    await state.update_data(
        {'count': count}
    )
    await message.answer("Отправьте фото товара")
    await Item.next()


@dp.message_handler(content_types=['photo'], state=Item.photo)
async def photo_def(message: types.Message, state: FSMContext):
    photo = message.photo[0].file_id
    await state.update_data(
        {'photo': photo})
    await message.answer('Теперь отправьте ссылку Фото\nСсылку для фото можно получить здесь\nhttps://postimages.org/', disable_web_page_preview=True)
    await Item.next()


@dp.message_handler(state=Item.photo_url)
async def photo_url_def(message: types.Message, state: FSMContext):
    photo_url = message.text
    await state.update_data(
        {'photo_url': photo_url})
    async with state.proxy() as data:
        kategory = data['kategory']
        name = data['name']
        info = data['info']
        price = data['price']
        count = data['count']
        photo = data['photo']
        await message.answer("Товар успешно был добавлен")
        insert_item(kategory, name, info, price, count, photo_url)
        await message.bot.send_photo(chat_id=message.from_user.id,
                                     photo=f'{photo}',
                                     caption=f'{kategory}\nНазвание товара {name}\nИнформация {info}\nСтоимость {price}\nКоличество товара {count}',
                                     reply_markup=menu_markup_def_admin)
    await state.finish()
