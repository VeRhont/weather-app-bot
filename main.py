import requests
import datetime
import random

from pprint import pprint
from config import OPEN_WEATHER_TOKEN, PATTERN, FORECAST_PATTERN
from weather_emojies import weather_emojies


def get_message(data):
    weather_description = data["weather"][0]["main"]
    wd = weather_emojies.get(weather_description, "Посмотри в окно")

    city_name = data["name"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

    current_date = datetime.datetime.today().strftime("%Y-%m-%d\t%H:%M")

    return PATTERN.format(current_date, city_name, temperature, wd, humidity, pressure, wind_speed,
                          sunset_timestamp)


def get_forecast_message(data):
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["main"]
    wd = weather_emojies.get(weather_description, "Посмотри в окно")

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

    return FORECAST_PATTERN.format(temperature, wd, humidity, pressure, wind_speed)


def get_current_weather(city, open_weather_token=OPEN_WEATHER_TOKEN):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang={'ru'}"
        )

        data = r.json()
        return get_message(data)

    except:
        return "☠️ Проверьте название города!"


def get_weather_in_random_city(open_weather_token=OPEN_WEATHER_TOKEN):
    while True:
        lat = random.randint(-90, 90)
        lon = random.randint(-180, 180)

        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric&lang={'ru'}"
            )

            data = r.json()

            if data["name"] != "":
                return get_message(data)
        except:
            return "☠️ Проверьте название города!"


def get_weather_forecast(city, open_weather_token=OPEN_WEATHER_TOKEN):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric&lang={'ru'}"
        )

        data = r.json()
        message = f"Погода в городе <b><em>{data['city']['name']}</em></b>\n"

        for day in data["list"]:
            if day["dt_txt"].endswith("15:00:00"):
                message += "\n"
                message += day["dt_txt"]
                message += get_forecast_message(day)

        return message

    except:
        return "☠️ Проверьте название города!"


def main():
    print(get_weather_forecast("Moscow"))


if __name__ == "__main__":
    main()
