import main


@main.bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    main.bot.reply_to(message, 'Hello world!')


@main.bot.message_handler(func=lambda message: True)
def echo_all(message):
    main.bot.reply_to(message, message.text)

print('im executed2')
print(main.bot)