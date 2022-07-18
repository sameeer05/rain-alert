import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "bd8bb4fea72a6d04aca4976f2c3d32fa"
account_sid = "AC9ee350521fc93979ab6fededf74d955f"
auth_token = "bf539bd70ff98f8df30aadf2621b3ffa"
my_coordinates = {"lat": 28.206600, "lon": 76.790901}

weather_params = {"lat": 17.968901, "lon": 79.594055, "exclude": "current,minutely,daily", "appid": api_key}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False

for i in range(0, 11):
    if data["hourly"][i]["weather"][0]["id"] < 800:
        will_rain = True
if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain today. Bring an umbrella.",
        from_="+18506608944",
        to="+919992057262"
    )
    print(message.status)
