from datetime import datetime
datetime_now = datetime.now().strftime("%d")


def get_tomorrow():
    datetime_tomorrow = int(datetime_now) + 1
    return datetime_tomorrow


url_today = "https://mirkosmosa.ru/lunar-calendar/phase-moon/lunar-day-today"
url_tomorrow = f"https://mirkosmosa.ru/lunar-calendar/phase-moon/2022/april/{get_tomorrow()}"

headers = {
    "Accept": "*/*",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
}