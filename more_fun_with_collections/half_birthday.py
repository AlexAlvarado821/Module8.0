"""
Author: Alex Alvarad
Program: half_birthday.py
Date: 10-18-20
Description: Returns the date 6 months after your birthday
"""
from datetime import datetime, timedelta

import datetime


def half_birthday(year, month, day):
    """
    :param year: Most recent birthday year
    :param month: Most recent birthday month
    :param day: Most recent birthday day
    :return: Half-year birthday date
    """
    mybirthday = datetime.datetime(year, month, day)
    half_year_later = mybirthday + timedelta(days=180)
    #180 days are approximately 6 months
    return str(half_year_later)









