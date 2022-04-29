from aiogram import types, Dispatcher
from keyboards import client_keyboard
from create_bot import bot
from aiogram.types import ReplyKeyboardRemove
from parse import lunar_calendar





# @dp.message_handler(commands="start")
async def start_message(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приветствую, нажмите на любую клавишу", reply_markup=client_keyboard.client_start_kb)
        await message.delete()
    except:
        await message.answer("Общение с ботом только через ЛС, напишите ему \n https://t.me/templateiogram_test_bot")

async def main_button(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы на главной странице")
async def settings_button(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы в настройках")

async def lunar_calendar_button(message: types.Message):
    await bot.send_message(message.from_user.id, "Please pick up your date",reply_markup=client_keyboard.client_lunar_kb)

async def get_lunar_calendar_today(message: types.Message):
    await bot.send_message(message.from_user.id, f"{lunar_calendar.bot_message_today}", reply_markup=client_keyboard.client_start_kb)

async def get_lunar_calendar_tomorrow(message: types.Message):
    await bot.send_message(message.from_user.id, f"{lunar_calendar.bot_message_tomorrow}", reply_markup=client_keyboard.client_start_kb)



# регистрируем обработчик
def register_message_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands="start")
    dp.register_message_handler(main_button, commands="Main")
    dp.register_message_handler(settings_button, commands=["Settings"])
    dp.register_message_handler(lunar_calendar_button, commands=["LunarCalendar"])
    dp.register_message_handler(get_lunar_calendar_today, commands=["Today"])
    dp.register_message_handler(get_lunar_calendar_tomorrow, commands=["Tomorrow"])
