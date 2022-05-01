from aiogram import types, Dispatcher
from keyboards import client_keyboard
from create_bot import bot
from aiogram.types import ReplyKeyboardRemove
from parse import lunar_calendar
from aiogram.dispatcher.filters import Text
from openweather import main







# @dp.message_handler(commands="start")
async def start_message(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приветствую, нажмите на любую клавишу", reply_markup=client_keyboard.client_start_kb)
        await message.delete()
    except:
        await message.answer("Общение с ботом только через ЛС, напишите ему \n https://t.me/templateiogram_test_bot")

async def main_button(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут пока ничего нет")
async def settings_button(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут пока ничего нет")

async def get_cookies(message: types.Message):
    await bot.send_message(message.from_user.id, "Choose directory",reply_markup=client_keyboard.client_keyboard_cookies)

async def get_lunar_data(message: types.Message):
    await bot.send_message(message.from_user.id, f"{lunar_calendar.answer_for_client}", reply_markup=client_keyboard.client_start_kb)

async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, f"{main.data}", reply_markup=client_keyboard.client_start_kb)









# регистрируем обработчик
def register_message_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands="start")
    dp.register_message_handler(main_button, commands="Main")
    dp.register_message_handler(settings_button, commands=["Settings"])
    dp.register_message_handler(get_cookies, Text(equals="Cookies", ignore_case=True))
    dp.register_message_handler(get_lunar_data, Text(equals="LunarCalendar", ignore_case=True))
    dp.register_message_handler(get_weather, Text(equals="GetWeather", ignore_case=True))




