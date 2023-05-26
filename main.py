import threading
import time


def start_flask():
    from app import app
    app.app.run(host='0.0.0.0', port=5000)


def start_tgBot():
    from tgBot import tgBot
    # Запускаем бота
    tgBot.bot.polling()


def main():
    flask_tread = threading.Thread(target=start_flask, name="flask")
    tgBot_tread = threading.Thread(target=start_tgBot, name="tgBot")

    flask_tread.start()
    tgBot_tread.start()

    thread_dict = {"flask": flask_tread, "tgBot": tgBot_tread}

    while True:
        # проходимся по объектам потоков
        for thread in threading.enumerate():
            # если поток умер
            if not thread.is_alive():
                print(f'Поток, читающий {thread.name} умер')
                # получаем из словаря `thread_dict`
                # поток по имени для его перезапуска
                restart = thread_dict[thread.name]
                # пытаемся перезапустить
                restart.start()
        time.sleep(1)


if __name__ == "__main__":
    main()
