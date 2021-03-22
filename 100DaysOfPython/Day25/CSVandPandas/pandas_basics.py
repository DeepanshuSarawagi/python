import pandas

with open("weather_data.csv", "r") as data_file:
    data = pandas.read_csv(data_file)
    print(data)
    print()
    print(data["temp"])

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))

# Dataframes methods basics

d = {
    "one": [1.0, 2.0, 3.0, 4.0],
    "two": [4.0, 2.0, 1.0, 3.0]
     }

data = pandas.DataFrame(d)
print(data)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temperature_list = data["temp"].to_list()
print(temperature_list)

sum_of_temp = 0

for temp in temperature_list:
    sum_of_temp += temp

average_temp = sum_of_temp / len(temperature_list)
print("{:.2f}".format(average_temp))

# We can use Series.mean method to get the mean value of a Series data
average_temp = data["temp"].mean()   # We can call the mean method here because data type of data["temp"] is Series
print(average_temp)
max_temp = data["temp"].max()
print(max_temp)

# We can use pandas to print the column values of a csv by just calling it as an attribute. For example

print(data.day)
print(data.temp)
print(data.condition)
