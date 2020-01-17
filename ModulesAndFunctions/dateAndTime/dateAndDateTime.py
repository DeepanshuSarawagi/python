import time

print("The epoch time of this system is at " + time.strftime("%c", time.gmtime(0)))
print(f"The current timezone is {time.tzname[0]} and the offset is {time.timezone}")

if time.daylight != 0:
    print("\t The Day Light Savings is in effect in this time zone")
    print("\t The Day Light Savings time is {}".format(time.tzname[1]))
else:
    print("\t The Day Light Savings is not in effect in this time zone")

print("The UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("The locale time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import datetime

print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.today())
