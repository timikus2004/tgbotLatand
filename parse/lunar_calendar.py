from datetime import datetime
import requests
from bs4 import BeautifulSoup
from parse.url_lunar import url_today, url_tomorrow, headers
import lxml

datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M')


def get_data_today():

    req = requests.get(url=url_today, headers=headers)

    src_today = req.text

    with open('index_today.html', 'w') as file:
        file.write(src_today)
#
#
def get_data_tomorrow():
    req = requests.get(url=url_tomorrow, headers=headers)

    src_tomorrow = req.text
    print(src_tomorrow)
    with open('index_tomorrow.html', 'w') as file:
        file.write(src_tomorrow)

#
#

def parse_date_today():
    with open('/home/timikus2004/PycharmProjects/tgbot_aiogram/parse/index_today.html') as file:
        src_today = file.read()

    soup = BeautifulSoup(src_today, "lxml")
    my_data_normal = soup.find_all(class_="moon_desc_normal")
    my_data_plus = soup.find_all(class_="moon_desc_plus")


    data_string_plus = ""
    data_string_normal = ""

    for item in my_data_plus:
        data_string_plus += item.text + "\n"
    for item in my_data_normal:
        data_string_normal += item.text + "\n"

    starting_message_today = f"Лунный календарь на сегодня:\n "
    parse_message_today = f"{starting_message_today}" + f"\n{data_string_plus}" + f"\n{data_string_normal}"
    return parse_message_today
#
#
#
#
def parse_date_tomorrow():
    with open('/home/timikus2004/PycharmProjects/tgbot_aiogram/parse/index_tomorrow.html') as file:
        src_tomorrow = file.read()

    soup = BeautifulSoup(src_tomorrow, "lxml")

    my_data_start = soup.find_all(class_="moon_desc_plus")
    my_data_normal = soup.find_all(class_="moon_desc_normal")


    # data_string_start = my_data_start[1].text
    # data_string_end = my_data_start[2].text
    data_string_start = ""
    for item in my_data_start:
        data_string_start += item.text

    data_string_normal = ""
    for item in my_data_normal:
        data_string_normal += item.text


    starting_message_tomorrow = f"Лунный календарь на завтра:\n "
    parse_message_tomorrow = f"{starting_message_tomorrow}" + f"\n{data_string_start}" \
                              + f"\n{data_string_normal}"
    return parse_message_tomorrow
#
#
# # данные для бота
bot_message_today = parse_date_today()

bot_message_tomorrow = parse_date_tomorrow()













