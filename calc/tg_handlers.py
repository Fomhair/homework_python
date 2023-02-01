from telegram import Update
from telegram.ext import ContextTypes
import parse
from my_math import calc as c


async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = '/calc <YOUR EXPRESSION>\n' \
             'The bot supports floating point numbers \n' \
             'and the following arithmetic operations: \n' \
             '(), ^, /, *, -, +'
    await update.message.reply_text(f'{result}')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    line = update.message.text
    formula = parse.get_formula(line)
    result = c.calc(formula)
    await update.message.reply_text(f'{result}')
