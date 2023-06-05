import requests


def geocode(place_name):
    url = f"https://geocode-maps.yandex.ru/1.x/?geocode={place_name + 'Тюмень'}&apikey=d2b18a08-c065-4ce2-8857-56d470457e15&format=json"

    # Отправка запроса к Nominatim
    response = requests.get(url)
    data = response.json()
    return ' '.join(data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()[::-1])
