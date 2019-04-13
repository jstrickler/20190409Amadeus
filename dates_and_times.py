#!/usr/bin/env python
from datetime import datetime, date, time, timedelta

today = date.today()
print(today.year, today.month, today.day)
print(today)

james_bd = date(2014, 8, 1)
print(james_bd)

diff = today - james_bd

age = diff.days / 365.25
print("James is {:.2f} years old".format(age))

years, days = divmod(diff.days, 365)

print("James is {} years and {} days old".format(
    years, days
))

print(today.strftime("%B %Y"))


print(today.weekday())
