from datetime import datetime

def is_today(date : datetime) -> bool:
    return date.date() == datetime.today().date()
