import pytz
import datetime

for x in pytz.country_names:
    print("{}: {}: {}  ".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

count = 0
while count < 10:
    available_time_zone = input(" Please select the two letter country code to get the date, time and timezone"
                                " and the UTC offset: ")
    if available_time_zone in pytz.country_names:
        if available_time_zone == 'BV':
            print("This country has no time zone defined")
            break
        for zone in pytz.country_timezones[available_time_zone]:
            time_zone = pytz.timezone(zone)
            world_time = datetime.datetime.now(tz=time_zone)
            local_time = datetime.datetime.now()
            utc_time = datetime.datetime.utcnow()
            print("world time in {}n is {} and the timezone is {} ".format(time_zone,
                                                                           world_time.strftime("%A %x %X %z"),
                                                                           world_time.tzname()))
            print("The local time is {} ".format(local_time))
            print("UTC time is {}".format(utc_time))

    count += 1

print("You have either selected nine time zones or a country code with no time zone defined area. "
      "Please come back after some time")
