from telegram.ext import ApplicationBuilder, CommandHandler
from tg_handlers import *
import configparser

config = configparser.ConfigParser()
config.read('token.ini')

app = ApplicationBuilder().token(config['DEFAULT']['token']).build()

app.add_handler(CommandHandler("help", commands))
app.add_handler(CommandHandler("Calc", calculate))

app.run_polling()
