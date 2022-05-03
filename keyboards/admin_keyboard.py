from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

load_btn = KeyboardButton("/deploy")
delete_btn = KeyboardButton("/cancel")
admin_set_data_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_set_data_kb.row(load_btn, delete_btn)