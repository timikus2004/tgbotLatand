import os
from dotenv import load_dotenv


load_dotenv()
# принимаем значение токена
OPEN_WEATHER_TOKEN = os.getenv("OPEN_WEATHER_TOKEN")

