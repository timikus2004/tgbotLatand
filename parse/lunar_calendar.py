from datetime import datetime
import requests
from bs4 import BeautifulSoup
from parse.url_lunar import url, headers, YEAR, MONTH, DAY




datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M')


def get_data():
    req = requests.get(url=url, headers=headers)
    source = req.text
    with open('/home/timikus2004/PycharmProjects/tgbot_aiogram/parse/index.html', 'w') as file:
        file.write(source)


def parsing_data():
    with open('/home/timikus2004/PycharmProjects/tgbot_aiogram/parse/index.html') as file:
        source = file.read()
    soup = BeautifulSoup(source, "lxml")
    soup_data_class_normal = soup.find_all(class_="moon_desc_normal")
    soup_data_class_plus = soup.find_all(class_="moon_desc_plus")

    my_data = ""

    for item in soup_data_class_normal:
        my_data += item.text + "\n"
    for item in soup_data_class_plus:
        my_data += item.text + "\n"

    hello_msg = f"Лунный календарь на {DAY} {MONTH} 20{YEAR}:\n "
    parse_message_today = f"{hello_msg}" + f"\n{my_data}"
    return parse_message_today

#
#
# # данные для бота
answer_for_client = parsing_data()















