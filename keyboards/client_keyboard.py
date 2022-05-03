import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# создание кнопок
cookie_btn = KeyboardButton(emoji.emojize(':cookie:') + "cookies")
menu_btn = KeyboardButton("menu")

# создание клавиатуры Введите one_time_keyboard=True чтобы сделать клавиатуру одноразовой
client_main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
# добавление кнопок в клавиатуру
# client_start_kb.add(b1).add(b2).insert(b3)
# расположение кнопок в строку
client_main_kb.row(cookie_btn, menu_btn)



# Parsing data from browser
lunar_btn = KeyboardButton(emoji.emojize(':waning_gibbous_moon:') + 'lunarCalendar')
get_weather_btn = KeyboardButton(emoji.emojize(':sun_behind_small_cloud:') + 'getWeather')
back_btn = KeyboardButton(emoji.emojize(':left_arrow:') + 'back')
share_contact_btn = KeyboardButton("share contact", request_contact=True)
share_geo_btn = KeyboardButton("share geolocation", request_location=True)
client_keyboard_cookies = ReplyKeyboardMarkup(resize_keyboard=True)
client_keyboard_cookies.row(lunar_btn, get_weather_btn)
client_keyboard_cookies.row(share_contact_btn, share_geo_btn)
client_keyboard_cookies.add(back_btn)


# back keyboard button
back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
back_kb.add(back_btn)



# if __name__ == "__main__":

#     print(emoji.emojize(':thumbs_up:'))


