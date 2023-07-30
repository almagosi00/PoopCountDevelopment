import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

import readWrite as rw

token = "6483792175:AAG8_iG8JdNo66QfqTNppPLeRXTfHcVaJHs"
poopEmoji = '\U0001F4A9'


logging.basicConfig(
    format='%(acstime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def poop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if(update.message.text == poopEmoji):
        rw.add(update.message.from_user.first_name,update.message.date)

async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= rw.count()
        )
    except:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "no hay cagadas"
        )

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        rw.clear()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "GRACIAS POR TIRAR DE LA CISTERNA"
        )
    except:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "base de datos pendiente de revisión"
        )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Ni puta idea de lo que dices Hulio."
    )

async def print(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= update.message.chat.title
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    poop_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), poop)
    count_handler = CommandHandler('count',count)
    clear_handler = CommandHandler('clear',clear)
    printr_handler = CommandHandler('print',print)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(poop_handler)
    application.add_handler(count_handler)
    application.add_handler(clear_handler)
    application.add_handler(printr_handler)
    application.add_handler(unknown_handler) # siempre el último en ser añadido

    

    application.run_polling()