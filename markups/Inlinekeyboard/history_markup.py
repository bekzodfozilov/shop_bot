from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup_history = InlineKeyboardMarkup()

markup_history.row(InlineKeyboardButton('❌ В ожидании', callback_data='waiting'), InlineKeyboardButton('✅ Принятые', callback_data='history'))

