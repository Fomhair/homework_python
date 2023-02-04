from telegram import Update
from telegram.ext import ContextTypes
import parse
from my_math import calc as c


async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = f'Hi, {update.effective_user.full_name}!\n' \
             'The bot supports floating point numbers \n' \
             'and the following arithmetic operations: \n' \
             '(), ^, /, *, -, + \n\n' \
             'For example: \n' \
             '-1 + 0.5 / (1 + 2) \n\n' \
             'And two trigonometric operations:\n' \
             'c as cos and s as sin\n' \
             's((c90)+(s59)) \n\n' \
             'Constants:\n' \
             'p, e'
    await update.message.reply_text(f'{result}')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    line = update.message.text
    formula = parse.get_formula(line)
    result = c.calc(formula)
    await update.message.reply_text(f'{result}')
