import time

print(time.gmtime(0))  # This will print the epoch time of this system which is usually January 1, 1970

print(time.localtime())  # This will print the local time

print(time.time())  # This will print the time in seconds since epoch time

time_here = time.localtime()

print(time_here)
for i in time_here:
    print(i)

print(time_here[0])
