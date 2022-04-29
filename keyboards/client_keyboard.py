from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# создание кнопок
b1 = KeyboardButton('/Main')
b2 = KeyboardButton("/Settings")
b3 = KeyboardButton("/LunarCalendar")
b4 = KeyboardButton("Share contact", request_contact=True)
b5 = KeyboardButton("Share geolocation", request_location=True)
# создание клавиатуры Введите one_time_keyboard=True чтобы сделать клавиатуру одноразовой
client_start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
# добавление кнопок в клавиатуру
# client_start_kb.add(b1).add(b2).insert(b3)
# расположение кнопок в строку
client_start_kb.row(b1, b2, b3)
client_start_kb.row(b4, b5)


# Parsing data from browser
lunar_button_today = KeyboardButton('/Today')
lunar_button_tomorrow = KeyboardButton('/Tomorrow')
client_lunar_kb = ReplyKeyboardMarkup(resize_keyboard=True)
client_lunar_kb.row(lunar_button_today, lunar_button_tomorrow)



