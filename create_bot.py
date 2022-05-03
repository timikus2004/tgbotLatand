import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()
storage = MemoryStorage()


# принимаем значение токена
TOKEN = os.getenv("TOKEN")
# создаем объект бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot= bot, storage=storage)
