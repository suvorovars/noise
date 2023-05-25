import threading


def start_flask():
    from app import app
    app.app.run(host='0.0.0.0', port=5000)


def start_tgBot():
    from tgBot import tgBot
    # Запускаем бота
    tgBot.bot.polling()


def main():
    flask_tread = threading.Thread(target=start_flask)
    tgBot_tread = threading.Thread(target=start_tgBot)
    flask_tread.start()
    tgBot_tread.start()


if __name__ == "__main__":
    main()
