import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print(f"The time in country {country} is {local_time}")
print(f"The UTC time is {datetime.datetime.utcnow()}")

for x in pytz.all_timezones:
    print(x)                   # This will print all the timezones which pytz.timezone() method will accept

for x in pytz.country_names:
    print(x + ": " + pytz.country_names[x])  # This will print all the country codes and country names

print("=" * 50)

# for x in sorted(pytz.country_names):
#     print(f"{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}")

for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}", end=': ')
    if x in pytz.country_timezones:
        print(f"{pytz.country_timezones[x]}")
    else:
        print("No time zones defined")
