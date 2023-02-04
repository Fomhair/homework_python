from telegram.ext import \
    ApplicationBuilder, CommandHandler, MessageHandler, filters
from tg_handlers import *
import configparser


config = configparser.ConfigParser()
config.read('token.ini')

app = ApplicationBuilder().token(config['DEFAULT']['token']).build()

app.add_handler(CommandHandler(["start", "help"], commands))
calc_handler = MessageHandler(filters.TEXT, calculate)
app.add_handler(calc_handler)

app.run_polling()
