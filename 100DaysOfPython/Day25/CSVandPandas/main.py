import csv

with open("weather_data.csv", "r") as data:
    output = csv.reader(data)
    for out in output:
        if out[1] == "temp":
            continue
        else:
            print(out[1])

print()

weather_forecast = []
with open("weather_data.csv", "r") as data_file:
    data = data_file.read()
    data = data.strip("\n")
    data = data.split("\n")
    print(data)
    for d in data:
        weather_forecast.append(d)
    # new_data = data.split(",")
    # print(new_data)
    # print()
    #
    # for data in new_data:
    #     data = data.strip("\n")
    #     print(data)

print()
print(weather_forecast)

weather_data = []
for d in weather_forecast:
    d = d.split(",")    # Always remember, splitting a string with a character will return a string
    weather_data.append(d)
print(weather_data)
