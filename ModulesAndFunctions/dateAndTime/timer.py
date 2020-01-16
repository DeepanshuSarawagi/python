import time
# from time import time as my_timer
from time import perf_counter as my_timer  # This will calculate the precise elapsed time
# from time import process_time as my_timer   # This will calculate the time taken by CPU to execute the code
import random

input("Please enter to start")
wait_time = random.randint(1, 6)  # initialising the wait time randomly between 1 and 6 seconds
time.sleep(wait_time)             # Asking the program to sleep
start_time = my_timer()           # Started the timer
input("Press enter to stop")      # asking user to stop
end_time = my_timer()             # calculating end time and storing it in variable

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print(f"Reaction time was {end_time - start_time}")

"""Display information about different .get_clock_info() method"""

print("time()\t\t\t", time.get_clock_info('time'))
print("perf_counter()\t", time.get_clock_info('perf_counter'))
print("monotonic()\t\t", time.get_clock_info('monotonic'))
print("process_time()\t", time.get_clock_info('process_time'))
