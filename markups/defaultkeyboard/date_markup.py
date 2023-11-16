import datetime

from aiogram.types import ReplyKeyboardMarkup


day = datetime.datetime.now().date().day
month = datetime.datetime.now().date().month
year = datetime.datetime.now().date().year

date1 = str(year) + '-' + str(month) + '-' + str(day)
date2 = str(year) + '-' + str(month) + '-' + str(day + 1)
date3 = str(year) + '-' + str(month) + '-' + str(day + 2)

date_markup = ReplyKeyboardMarkup(resize_keyboard=True)

date_markup.row(date1, date2, date3)
date_markup.add('🔚 Главный меню')


