import datetime
import requests
# from pprint import pprint
from openweather.create_api import OPEN_WEATHER_TOKEN
city_data = "kazan"


def get_weather(city_name, token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={token}&units=metric")
        data = r.json()
        # pprint(data)
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        weather =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n" +
            f"Погода в городе : {city}\n " +
            f"Температура : {temp} °С\n" +
            f" Влажность : {humidity} %\n" +
            f" Давление: {pressure} мм.рт.ст.\n" +
            f" Ветер: {wind} м/сек\n" +
            f" Рассвет: {sunrise}\n" +
            f" Закат: {sunset}\n" +
            f"Хорошего дня!")
        return weather


    except Exception as ex:
        print(ex)
        print("Введите название города")

def main():
    return get_weather(city_data, OPEN_WEATHER_TOKEN)


data = main()


