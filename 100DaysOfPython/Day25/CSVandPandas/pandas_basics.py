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
