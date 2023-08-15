import requests
import datetime
import random

from config import OPEN_WEATHER_TOKEN, PATTERN
from weather_emojies import weather_emojies


def get_message(data):
    weather_description = data["weather"][0]["main"]
    wd = weather_emojies.get(weather_description, "Посмотри в окно")

    city_name = data["name"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    length_of_the_day = sunset_timestamp - sunrise_timestamp

    current_date = datetime.datetime.today().strftime("%Y-%m-%d\t%H:%M")

    return PATTERN.format(current_date, city_name, temperature, wd, humidity, pressure, wind_speed, sunrise_timestamp,
                          sunset_timestamp, length_of_the_day)


def get_weather(city, open_weather_token=OPEN_WEATHER_TOKEN):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang={'ru'}"
        )

        data = r.json()
        return get_message(data)

    except:
        return "☠️ Проверьте название города!"


def get_weather_in_random_city(open_weather_token=OPEN_WEATHER_TOKEN):
    lat = random.randint(-90, 90)
    lon = random.randint(-180, 180)

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric&lang={'ru'}"
        )

        data = r.json()
        return get_message(data)

    except:
        return "☠️ Проверьте название города!"


def main():
    city = input("Введите название города: ")
    print(get_weather(city, OPEN_WEATHER_TOKEN))


if __name__ == "__main__":
    main()
