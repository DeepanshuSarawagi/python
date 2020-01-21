import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time is {local_time}")
print(f"Naive utc time is {utc_time}")

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time is {aware_local_time}, time zone is {aware_local_time.tzinfo}")
print(f"Aware utc time is {aware_utc_time}, time zone is {aware_utc_time.tzinfo}")
