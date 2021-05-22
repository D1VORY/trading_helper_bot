from settings import bot


if __name__ == '__main__':
    import handlers.message
    print('Starting polling...')
    print(bot)
    bot.polling()
