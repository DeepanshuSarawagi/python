import pandas
import random

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

print()
# How to print a specific column of data
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

# We can create data as objects and access it's data as attributes

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp
monday_temp = monday_temp * (9/5) + 32
print(monday_temp)

print(data[data.condition == "Sunny"])

# In this lesson we are going to learn how to loop through Pandas Dataframe

student_dict = {
    "Student": ["Deepanshu", "Divya", "Rajat", "Vandana"],
    "Score": [random.randint(50, 100) for i in range(0, 4)]
}
print(student_dict)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.Student)
    print(row.Score)

for index, row in student_data_frame.iterrows():
    if row.Score > 65:
        print(row.Student)
