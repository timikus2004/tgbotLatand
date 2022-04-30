from datetime import datetime
datetime_now = datetime.now().strftime("%d")


from datetime import datetime
datetime_now = datetime.now().strftime("%d")

months = {
    "01": "january",
    "02": "february",
    "03": "march",
    "04": "april",
    "05": "may",
    "06": "june",
    "07": "july",
    "08": "august",
    "09": "september",
    "10": "october",
    "11": "november",
    "12": "december"
}

def get_year():
    year = datetime.now().strftime("%y")
    return year

def get_month():
    month = datetime.now().strftime("%m")
    return month


def get_day():
    day = datetime.now().strftime("%d")
    return day

YEAR = get_year()
MONTH = months[f"{get_month()}"]
DAY = get_day()



url= f"https://mirkosmosa.ru/lunar-calendar/phase-moon/20{YEAR}/{MONTH}/{DAY}"
headers = {
    "Accept": "*/*",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
}


