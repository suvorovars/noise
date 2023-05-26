import requests


def geocode(place_name):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={place_name}"

    # Отправка запроса к Nominatim
    response = requests.get(url)
    data = response.json()

    # Проверка наличия результатов
    if len(data) > 0:
        # Извлечение координат из ответа
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        return latitude, longitude
    else:
        # Если результатов нет, возвращаем None
        return None, None


# Пример использования функции
place_name = "Тюмень заречный"

latitude, longitude = geocode(place_name)
if latitude is not None and longitude is not None:
    print(f"Координаты для места '{place_name}':")
    print("Широта:", latitude)
    print("Долгота:", longitude)
else:
    print("Не удалось найти координаты для указанного места.")
