from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# создание кнопок
b1 = KeyboardButton('/Main')
b2 = KeyboardButton("/Settings")
b3 = KeyboardButton("Cookies")
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
lunar_btn = KeyboardButton('LunarCalendar')
empty_btn1 = KeyboardButton('GetWeather')
empty_btn2 = KeyboardButton('empty2')
empty_btn3 = KeyboardButton('empty3')
client_keyboard_cookies = ReplyKeyboardMarkup(resize_keyboard=True)
client_keyboard_cookies.row(empty_btn1, empty_btn2, empty_btn3).insert(lunar_btn)





