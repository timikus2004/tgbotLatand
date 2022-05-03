from aiogram import Dispatcher, types
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from sqlite_db import sqlite_db
from aiogram.dispatcher.filters import Text
from keyboards import admin_keyboard
from keyboards import client_keyboard


class FSMstorage(StatesGroup):
    username = State()
    age = State()
    city = State()

# @dp.message_handler(commands=["moderator"], is_chat_admin=True)
async def make_changes(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "moderate mode is ON!", reply_markup=admin_keyboard.admin_set_data_kb)
    await message.delete()

# @dp.message_handler(commands=["cancel"],state="*")
# @dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")



# @dp.message_handler(commands=["moderator"])
async def set_data_to_db(message: types.Message):
    if message.from_user.id == ID:
        await FSMstorage.username.set()
        await message.reply("enter your name in latin")


async def cancel(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return


# @dp.message_handler(state=FSMstorage.username)
async def set_username(message: types.Message, state= FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["username"] = message.text
        await FSMstorage.next()
        await message.reply("how old are you?")

# # @dp.message_handler(lambda message: message.text.isdigit(), state=FSMstorage.age)
# async def invalid_set_age(message: types.Message, state= FSMContext):
#     if message.from_user.id == ID:
#         return await message.reply("Age gotta be a number.\n How old are you? (digits only)")

# @dp.message_handler(lambda message: message.text.isdigit(), state=FSMstorage.age)
async def set_age(message: types.Message, state= FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["age"] = message.text
        await FSMstorage.next()
        await message.reply("city you live?")

# @dp.message_handler(state=FSMstorage.city)
async def set_city(message: types.Message, state= FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["city"] = message.text

        await sqlite_db.set_data(state)
        await bot.send_message(message.from_user.id, "new data was ADDED!")
        await state.finish()






def register_message_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes, commands=["moderator"], is_chat_admin=True)
    dp.register_message_handler(set_data_to_db, commands=["deploy"])
    dp.register_message_handler(cancel, commands=["cancel"], state="*")
    dp.register_message_handler(cancel, Text(equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(set_username, state=FSMstorage.username)
    # dp.register_message_handler(invalid_set_age, lambda message: message.text.isdigit(), state=FSMstorage.age)
    dp.register_message_handler(set_age, lambda message: message.text.isdigit(), state=FSMstorage.age)
    dp.register_message_handler(set_city, state=FSMstorage.city)
