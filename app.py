from aiogram import executor
from create_bot import dp
from handlers import client

# функция при запуске
async def on_startup(_):
    print("bot is working...")

# вызываем регистратор хендлера
client.register_message_handlers_client(dp)

# точка входа в наш скрипт
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)