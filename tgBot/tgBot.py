import telebot
import sqlite3

# Устанавливаем соединение с базой данных в виде пула соединений
conn = sqlite3.connect('db/main.db', check_same_thread=False)
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS survey (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        place TEXT,
        mainNoise TEXT,
        frequency_in_noisy_place INTEGER,
        noise_rating INTEGER,
        noise_impact_rating INTEGER,
        illness_from_noise TEXT,
        sleep_problem INTEGER,
        noise_control_measures TEXT
    )
''')
conn.commit()

# Создаем объект бота
bot = telebot.TeleBot('5304249209:AAHhX0N6Imj0e6FuNNlWG3XZfwO5-0sYLXk')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Пожалуйста, ответьте на несколько вопросов.")

    # Запрашиваем возраст
    bot.send_message(message.chat.id, "Введите ваш возраст:")
    bot.register_next_step_handler(message, ask_place)

def ask_place(message):
    # Сохраняем возраст в базу данных
    age = message.text
    cursor.execute('INSERT INTO survey (age) VALUES (?)', (age,))
    conn.commit()

    # Запрашиваем место проживания
    bot.send_message(message.chat.id, "Введите место вашего проживания:")
    bot.register_next_step_handler(message, ask_main_noise)

def ask_main_noise(message):
    # Сохраняем место проживания в базу данных
    place = message.text
    cursor.execute('UPDATE survey SET place = ? WHERE id = (SELECT MAX(id) FROM survey)', (place,))
    conn.commit()

    # Отправляем пользователю кнопки для выбора источника шума
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Строительные работы', 'Детский сад/школа/детские площадки', 'Трасса',
               'Наличие рядом аэропорта/железнодорожных путей', 'Шумные соседи', 'Шум в общественном транспорте',
               'Наличие клубов/баров/шумных кафе рядом с домом')
    bot.send_message(message.chat.id, "Что для вас является главным источником шума в районе, где вы проживаете?",
                     reply_markup=markup)
    bot.register_next_step_handler(message, ask_frequency_in_noisy_place)

def ask_frequency_in_noisy_place(message):
    # Сохраняем выбранный источник шума в базу данных
    main_noise = message.text
    cursor.execute('UPDATE survey SET mainNoise = ? WHERE id = (SELECT MAX(id) FROM survey)', (main_noise,))
    conn.commit()

    # Запрашиваем частоту нахождения в шумном месте
    bot.send_message(message.chat.id, "Как часто вы находитесь в шумном месте? (Введите число раз в неделю):")
    bot.register_next_step_handler(message, ask_noise_rating)

def ask_noise_rating(message):
    # Сохраняем частоту нахождения в шумном месте в базу данных
    frequency_in_noisy_place = message.text
    cursor.execute('UPDATE survey SET frequency_in_noisy_place = ? WHERE id = (SELECT MAX(id) FROM survey)',
                   (frequency_in_noisy_place,))
    conn.commit()

    # Запрашиваем оценку шума
    bot.send_message(message.chat.id, "Пожалуйста, оцените шум по шкале от 1 до 10 (1 - минимальный шум, 10 - максимальный шум):")
    bot.register_next_step_handler(message, ask_noise_impact_rating)

def ask_noise_impact_rating(message):
    # Сохраняем оценку шума в базу данных
    noise_rating = message.text
    cursor.execute('UPDATE survey SET noise_rating = ? WHERE id = (SELECT MAX(id) FROM survey)', (noise_rating,))
    conn.commit()

    # Запрашиваем оценку влияния шума
    bot.send_message(message.chat.id, "Пожалуйста, оцените влияние шума на ваше здоровье по шкале от 1 до 10 "
                                      "(1 - минимальное влияние, 10 - максимальное влияние):")
    bot.register_next_step_handler(message, ask_illness_from_noise)

def ask_illness_from_noise(message):
    # Сохраняем оценку влияния шума на здоровье в базу данных
    noise_impact_rating = message.text
    cursor.execute('UPDATE survey SET noise_impact_rating = ? WHERE id = (SELECT MAX(id) FROM survey)',
                   (noise_impact_rating,))
    conn.commit()

    # Запрашиваем наличие заболеваний от шума
    bot.send_message(message.chat.id, "Есть ли у вас заболевания, связанные со шумом? Если да, опишите их.")
    bot.register_next_step_handler(message, ask_sleep_problem)

def ask_sleep_problem(message):
    # Сохраняем информацию о заболеваниях от шума в базу данных
    illness_from_noise = message.text
    cursor.execute('UPDATE survey SET illness_from_noise = ? WHERE id = (SELECT MAX(id) FROM survey)',
                   (illness_from_noise,))
    conn.commit()

    # Запрашиваем наличие проблем со сном
    bot.send_message(message.chat.id, "У вас есть проблемы со сном из-за шума? (Введите 1 - да, 0 - нет):")
    bot.register_next_step_handler(message, ask_noise_control_measures)

def ask_noise_control_measures(message):
    # Сохраняем информацию о проблемах со сном в базу данных
    sleep_problem = message.text
    cursor.execute('UPDATE survey SET sleep_problem = ? WHERE id = (SELECT MAX(id) FROM survey)', (sleep_problem,))
    conn.commit()

    # Запрашиваем меры по контролю шума
    bot.send_message(message.chat.id, "Какие меры по контролю шума вы предпринимаете?")
    bot.register_next_step_handler(message, save_survey)

def save_survey(message):
    # Сохраняем меры по контролю шума в базу данных
    noise_control_measures = message.text
    cursor.execute('UPDATE survey SET noise_control_measures = ? WHERE id = (SELECT MAX(id) FROM survey)',
                   (noise_control_measures,))
    conn.commit()

    # Завершаем опрос и благодарим пользователя
    bot.send_message(message.chat.id, "Спасибо за заполнение опроса! Ваши ответы сохранены.")


