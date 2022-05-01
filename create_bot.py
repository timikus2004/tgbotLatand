import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


load_dotenv()



# принимаем значение токена
TOKEN = os.getenv("TOKEN")
# создаем объект бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
