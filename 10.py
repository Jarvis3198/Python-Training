"""You have to get today's date, then calculate yesterday's or tomorrow's."""

from datetime import date,timedelta

today = date.today()
one_day = timedelta(days=1)

tomorrow = today + one_day
yesterday = today - one_day

print("Today's date:", today)
print("Yesterday's date:", yesterday)
print("Tomorrow's date:", tomorrow)