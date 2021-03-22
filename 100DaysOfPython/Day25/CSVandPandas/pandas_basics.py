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