no_of_days = int(input("How many day's temperature you want to calculate average for? "))
list_of_temps = []
count = 0
while count < no_of_days:
    temp = int(input("Enter Day {}'s temperature: ".format(count + 1)))
    list_of_temps.append(temp)
    count += 1

sum_of_temps = sum(list_of_temps)
average_temp = sum_of_temps / len(list_of_temps)

print("The average temperature of past {} days is {:.2f}.".format(no_of_days, average_temp))

high_temp_days = 0
for i in list_of_temps:
    if i > average_temp:
        high_temp_days += 1

print("{} days above average temperate".format(high_temp_days))
