from decouple import config
import telebot


TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
BINANCE_TOKEN = config('BINANCE_TOKEN')
BINANCE_SECRET_KEY = config('BINANCE_SECRET_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

USER_ID = ''
