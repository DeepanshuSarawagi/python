import requests
import datetime

parameters = {
    "lat": 13.082680,
    "lng": 80.270721,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(datetime.datetime.utcnow())

print("{}, {}".format(sunrise.split("T")[1].split("+")[0], sunset.split("T")[1].split("+")[0]))
