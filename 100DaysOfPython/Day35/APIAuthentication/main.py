import requests

parameters = {
    "lat":  "6.10",
    "lon":  "106.49",
    "exclude": "current,minutely,daily",
    "appid": "blahblah"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

for i in range(0, 12):
    print(data["hourly"][i]["weather"][0]["description"])