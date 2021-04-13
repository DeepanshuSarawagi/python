import datetime

utc_now = datetime.datetime.utcnow()
print(utc_now)
time_now = datetime.datetime.now()
year = time_now.year
month = time_now.month
day = time_now.day

print("Day {}, month is {} and year is {}".format(day, month, year))
