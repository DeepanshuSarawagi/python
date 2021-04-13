import datetime

utc_now = datetime.datetime.utcnow()
print(utc_now)
time_now = datetime.datetime.now()
year = time_now.year
month = time_now.month
day = time_now.day
weekday = time_now.weekday()
print("Day {}, date is {} month is {} and year is {}".format(weekday, day, month, year))
