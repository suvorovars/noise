def start_tgBot():
    from tgBot import tgBot
    # Запускаем бота
    tgBot.bot.polling()

if __name__ == '__main__':
    start_tgBot()