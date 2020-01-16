import time
from time import time as my_timer
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
