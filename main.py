from decouple import config
import telebot

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
BINANCE_TOKEN = config('BINANCE_TOKEN')
BINANCE_SECRET_KEY = config('BINANCE_SECRET_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

if __name__ == '__main__':
    import handlers.message
    print('Starting polling...')
    print(bot)
    bot.polling()
