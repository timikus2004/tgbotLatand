
from datetime import datetime
datetime_now = datetime.now().strftime("%d")


def get_tomorrow():
    datetime_tomorrow = int(datetime_now) + 1
    return datetime_tomorrow

date_tomorrow = get_tomorrow()