import telebot
import sqlite3

from telebot import types

# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('app/db/main.db', check_same_thread=False)
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS survey (
                    id INTEGER,
                    age INTEGER,
                    place TEXT,
                    mainNoise TEXT,
                    frequency_in_noisy_place INTEGER,
                    noise_rating INTEGER,
                    noise_impact_rating INTEGER,
                    illness_from_noise TEXT,
                    sleep_problem INTEGER,
                    noise_control_measures TEXT,
                    completed INTEGER DEFAULT 0
                )''')
conn.commit()

# Создаем объект бота
bot = telebot.TeleBot('5304249209:AAHhX0N6Imj0e6FuNNlWG3XZfwO5-0sYLXk')


# Определяем обработчик команды /start
@bot.message_handler(commands=['start'])
def start_survey(message):
    user_id = message.chat.id

    # Check if the user has already completed the survey
    cursor.execute('SELECT completed FROM survey WHERE id = ?', (user_id,))
    result = cursor.fetchone()

    if result and result[0] == 1:
        # User has already completed the survey
        bot.send_message(user_id, 'Вы уже прошли опрос. Благодарим за участие!')
    else:
        # User has not completed the survey
        bot.send_message(user_id, 'Укажите свой возраст:')
        bot.register_next_step_handler(message, ask_age)


# Определяем обработчик ответа на первый вопрос
def ask_age(message):
    chat_id = message.chat.id
    age = message.text

    # Записываем данные в базу данных
    cursor.execute('''INSERT INTO survey 
                    (id, age) 
                    VALUES (?, ?)''', (chat_id, age))
    conn.commit()

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # Добавление кнопок с вариантами ответа
    keyboard.add(types.KeyboardButton('Заречный Европейский'),
                 types.KeyboardButton('Дом Обороны'),
                 types.KeyboardButton('ТюмГУ'),
                 types.KeyboardButton('2 городская больница'),
                 types.KeyboardButton('Червишевский тракт'),
                 types.KeyboardButton('Заречный Югра'),
                 types.KeyboardButton('Другое'))

    bot.reply_to(message, "Отлично! Теперь укажите район, в котором вы проживаете.", reply_markup=keyboard)
    bot.register_next_step_handler(message, ask_place)


# Определяем обработчик ответа на второй вопрос
def ask_place(message):
    place = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET place = ? WHERE id = ?''', (place, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Что для вас является главным источником шума в районе, где вы проживаете?")
    bot.register_next_step_handler(message, ask_main_noise)


# Продолжайте добавлять обработчики для остальных вопросов в таком же формате

# Определяем обработчик ответа на третий вопрос
def ask_main_noise(message):
    main_noise = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET mainNoise = ? WHERE id = ?''', (main_noise, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Часто ли вы бываете в шумных местах?")
    bot.register_next_step_handler(message, ask_frequency_in_noisy_place)


# Определяем обработчик ответа на четвертый вопрос
def ask_frequency_in_noisy_place(message):
    frequency = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET frequency_in_noisy_place = ? WHERE id = ?''', (frequency, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Оцените по 10-бальной шкале уровень шумового загрязнения в месте, где вы проживаете?")
    bot.register_next_step_handler(message, ask_noise_rating)


# Продолжайте добавлять обработчики для остальных вопросов в таком же формате

# Определяем обработчик ответа на пятый вопрос
def ask_noise_rating(message):
    rating = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET noise_rating = ? WHERE id = ?''', (rating, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Оцените по 10-бальной шкале то, как шум влияет на ваше самочувствие?")
    bot.register_next_step_handler(message, ask_noise_impact_rating)


# Определяем обработчик ответа на шестой вопрос
def ask_noise_impact_rating(message):
    impact_rating = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET noise_impact_rating = ? WHERE id = ?''', (impact_rating, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Отметьте неблагоприятные влияния шума, которые вы на себе ощущаете.")
    bot.register_next_step_handler(message, ask_illness_from_noise)


# Продолжайте добавлять обработчики для остальных вопросов в таком же формате

# Определяем обработчик ответа на седьмой вопрос
def ask_illness_from_noise(message):
    illness = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET illness_from_noise = ? WHERE id = ?''', (illness, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Считаете ли вы, что у вас есть проблемы со сном?")
    bot.register_next_step_handler(message, ask_sleep_problem)


# Определяем обработчик ответа на восьмой вопрос
def ask_sleep_problem(message):
    sleep_problem = 0
    if message.text.lower().strip() == 'да':
        sleep_problem = 1

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET sleep_problem = ? WHERE id = ?''', (sleep_problem, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Какие меры вы знаете/применяете для борьбы с шумом на улице и дома?")
    bot.register_next_step_handler(message, ask_noise_control_measures)


# Определяем обработчик ответа на девятый вопрос
def ask_noise_control_measures(message):
    measures = message.text

    # Обновляем запись в базе данных
    cursor.execute('''UPDATE survey SET noise_control_measures = ?, completed = 1 WHERE id = ?''',
                   (measures, message.chat.id))
    conn.commit()

    bot.reply_to(message, "Спасибо за участие в опросе! Ваши ответы были записаны.")


