import requests
from datetime import datetime

API_KEY = "9290fe92b75fff605476d8faf912e41e" # Можете поменять на ваш API ключ OpenWeatherMap
CITY_ID = 1526384  # ID Алматы
URL = f"http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric&lang=ru" # Использовал этот URL для получения погоды в Алматы

def log(message):
    with open("weather_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")

def fetch_weather():
    try:
        log("📡 Запрос текущей погоды...")

        response = requests.get(URL)
        data = response.json()

        if response.status_code != 200 or data.get("cod") != 200:
            log(f"❌ Ошибка API: {data.get('message', 'Неизвестная ошибка')}")
            return

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Текущая погода в Алматы:\n"
            f"- {weather}\n"
            f"- Температура: {temp}°C (ощущается как {feels_like}°C)\n"
            f"- Влажность: {humidity}%\n"
            f"- Давление: {pressure} гПа\n"
            f"- Ветер: {wind_speed} м/с\n"
        )

        with open("weather_result.txt", "w", encoding="utf-8") as result_file:
            result_file.write(result)

        log("✅ Погода успешно получена и записана.")
    except Exception as e:
        log(f"⚠️ Ошибка выполнения: {str(e)}")

if __name__ == "__main__":
    fetch_weather()