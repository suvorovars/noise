# API для получения данных
Для получения данных опроса, сделайте запрос по адресу /api/generate_survey

#### ПРИМЕР:
http://185.46.9.123/api/generate_survey

Вы можете передавать аргументы для фильтрации и сортировки данных

## Параметры в API
http://185.46.9.123/api/generate_survey
- ?age=[\<int> / \<int>, \<int>]
- &age_comparison=\<string>
- &place=\<int> \<int>
- &main_noise=\<string>
- &frequency_in_noisy_place=[\<int> / \<int>, \<int>]
- &frequency_in_noisy_place_comparison=\<string>
- &noise_rating=[\<int> / \<int>, \<int>]
- &noise_rating_comparison=\<string>
- &noise_impact_rating=[\<int> / \<int>, \<int>]
- &noise_impact_rating_comparison=\<string>
- &illness_from_noise=\<string>
- &sleep_problem=\<int> 
- &noise_control_measures=\<string>
- &sort_key=\<string>

### age
параметр, отвечающий за фильтрацию пользователей по возрасту. Введите одно число, чтобы вывести ответы людей определённого возраста, или передайте 2 числа через запятую, чтобы получить ответы с возрастом в промежутке между этими числами. Используйте ключ **age_comparison** со значениями "less" или "greater", чтобы искать значения возраста меньше или больше числа, переданного в **age**.

#### Пример:
http://185.46.9.123/api/generate_survey?age=18&age_comparison=less
Вернёт ответы пользователей младше 18 лет.

http://185.46.9.123/api/generate_survey?age=17,19
Вернёт ответы пользователей в возрасте от 17 до 19 лет.

http://185.46.9.123/api/generate_survey?age=18
Вернёт пользователей возрастом 18 лет.

### place 
параметр, отвечающий за выбор места. Принимает на вход координаты через пробел.

#### Пример
http://185.46.9.123/api/generate_survey?place=57.158337+65.526149
Вернёт всех пользователей, указавших данные координаты.

### main_noise 
параметр, который позволяет фильтровать данные по основным источникам шума.

#### Пример
http://185.46.9.123/api/generate_survey?main_noise=дорога
Вернёт ответы всех пользователей, у которых основным источником шума является дорога.

### frequency_in_noisy_place
параметр, позволяющий фильтровать данные по частоте прибывания в шумных местах. Можно передать одно число, чтобы получить 
ответы с указанной частотой прибывания, или передать 2 числа через запятую, чтобы получить ответы с частотой в указанном 
диапазоне. Используйте ключ **frequency_in_noisy_place_comparison** со значениями "less" или "greater", 
чтобы искать значения частоты меньше или больше числа, переданного в **frequency_in_noisy_place**.

#### Пример:
http://185.46.9.123/api/generate_survey?frequency_in_noisy_place=5&frequency_in_noisy_place_comparison=greater
Вернёт ответы пользователей, у которых частота пребывания в шумном месте соотвествует числу 5.

http://185.46.9.123/api/generate_survey?frequency_in_noisy_place=2,4
Вернёт ответы пользователей, у которых частота пребывания в шумных местах соотвествует числам от 2 до 4.

### noise_rating
параметр, позволяющий фильтровать данные по оценке уровня шума. Можно передать одно число, чтобы получить ответы 
с указанной оценкой, или передать 2 числа через запятую, чтобы получить ответы с оценкой шума в указанном диапазоне.
Используйте ключ **noise_rating_comparison** со значениями "less" или "greater", чтобы искать значения оценки шума 
меньше или больше числа, переданного в **noise_rating**.

#### Пример:
http://185.46.9.123/api/generate_survey?noise_rating=7&noise_rating_comparison=greater
Вернёт ответы пользователей, у которых оценка уровня шума больше 7.

http://185.46.9.123/api/generate_survey?noise_rating=5,8&noise_rating_comparison=less
Вернёт ответы пользователей, у которых оценка уровня шума находится в диапазоне от 5 до 8.

### noise_impact_rating
параметр, позволяющий фильтровать данные по оценке воздействия шума. Можно передать одно число, чтобы получить ответы с 
указанной оценкой, или передать 2 числа через запятую, чтобы получить ответы с оценкой воздействия шума в указанном 
диапазоне. Используйте ключ **noise_impact_rating_comparison** со значениями "less" или "greater", чтобы искать 
значения оценки воздействия шума меньше или больше числа, переданного в **noise_impact_rating**.

#### Пример:
http://185.46.9.123/api/generate_survey?noise_impact_rating=6&noise_impact_rating_comparison=greater
Вернёт ответы пользователей, у которых оценка воздействия шума больше 6.

http://185.46.9.123/api/generate_survey?noise_impact_rating=4,7
Вернёт ответы пользователей, у которых оценка воздействия шума находится в диапазоне от 4 до 7.

### illness_from_noise
параметр, позволяющий фильтровать данные по наличию заболеваний, связанных со шумом.

#### Пример:
http://185.46.9.123/api/generate_survey?illness_from_noise=головная+боль
Вернёт ответы пользователей, у которых болит голова из-за шума.

### sleep_problem
параметр, позволяющий фильтровать данные по наличию проблем со сном. Можно передать число 0 или 1

#### Пример:
http://185.46.9.123/api/generate_survey?sleep_problem=1
Вернёт ответы пользователей, у которых есть проблемы со сном

### noise_control_measures
параметр, позволяющий фильтровать данные по принятым мерам по контролю над шумом. Можно передать строковое значение 
для поиска ответов пользователей, которые приняли указанные меры.

#### Пример:
http://185.46.9.123/api/generate_survey?noise_control_measures=шумопоглощающие+материалы
Вернёт ответы пользователей, которые приняли меры по использованию шумопоглощающих материалов.

### sort_key
параметр, позволяющий сортировать данные по указанному ключу. Можно передать строковое значение, чтобы отсортировать данные по определенному полю.

#### Пример:
http://185.46.9.123/api/generate_survey?sort_key=age
Вернёт ответы пользователей, отсортированные по возрасту.

http://185.46.9.123/api/generate_survey?sort_key=noise_rating
Вернёт ответы пользователей, отсортированные по оценке уровня шума.

## Полученный ответ
В итоге вы увидите .json файл следущего вида:
```
[ {
      "age":18,
      "frequency_in_noisy_place":4,
      "id":1491619914,
      "illness_from_noise":"Головная боль",
      "mainNoise":"Трасса",
      "noise_control_measures":"Наушники",
      "noise_impact_rating":8,
      "noise_rating":8,
      "place":"57.152985 65.541227",
      "sleep_problem":1
},
{
      "age":19,
      "frequency_in_noisy_place":-1,
      "id":871428143,
      "illness_from_noise":"головная боль",
      "mainNoise":"дороги",
      "noise_control_measures":"никаких",
      "noise_impact_rating":7,
      "noise_rating":7,
      "place":"57.126636 65.515787",
      "sleep_problem":1
},
{
      "age":17,
      "frequency_in_noisy_place":5,
      "id":1968149036,
      "illness_from_noise":"Ничего из этого",
      "mainNoise":"Трасса",
      "noise_control_measures":"Ничего из этого",
      "noise_impact_rating":0,
      "noise_rating":8,
      "place":"57.150191 65.591671",
      "sleep_problem":1
},
{
      "age":17,
      "frequency_in_noisy_place":4,
      "id":2106155418,
      "illness_from_noise":"Головная боль",
      "mainNoise":"Аэропорт/Железнодорожные пути",
      "noise_control_measures":"Наушники",
      "noise_impact_rating":7,
      "noise_rating":8,
      "place":"57.111859 65.523719",
      "sleep_problem":1
},
{
      "age":18,
      "frequency_in_noisy_place":4,
      "id":1290749687,
      "illness_from_noise":"Головная боль",
      "mainNoise":"Трасса",
      "noise_control_measures":"Наушники",
      "noise_impact_rating":4,
      "noise_rating":5,
      "place":"57.188304 65.571814",
      "sleep_problem":0
} ]
```

# API для загрузки картинок

Вы можете использовать следующий код:

```
import requests

url = 'http://185.46.9.123/api/upload'  # Замените адрес_сайта и порт на фактические значения

file_path = "путь_к_изображению"

sender_name = 'Имя отправителя'

caption = 'Подпись к изображению'

files = {'file': open(file_path, 'rb')}

data = {'sender_name': sender_name, 'caption': caption}

response = requests.post(url, files=files, data=data)

print(response.text)
```
