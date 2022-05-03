import logging
from aiogram import executor
from sqlite_db import sqlite_db
from create_bot import dp
from handlers import client, admin
from parse import lunar_calendar

logging.basicConfig(level=logging.INFO)

# функция при запуске
async def on_startup(_):
    print("bot is working...")
    await sqlite_db.create_db()
    lunar_calendar.get_data()


# вызываем регистратор хендлера
client.register_message_handlers_client(dp)
admin.register_message_handlers_admin(dp)

# точка входа в наш скрипт
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
