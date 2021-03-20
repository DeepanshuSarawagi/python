import csv

with open("weather_data.csv", "r") as data:
    output = csv.reader(data)
    for out in output:
        if out[1] == "temp":
            continue
        else:
            print(out[1])
