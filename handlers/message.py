from settings import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello! This bot helps you to store your trades.')
