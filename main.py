# Import statements
import datetime
import constance as keys
from telegram.ext import *
import random

# terminal notification of start up
print("Bot Started...")


def start_command(update, context):

    # choose a random number
    randomResponse = random.randint(1, 5)

    # set up appropriate datetime objects
    nowDT = datetime.datetime.now().time()
    morningDT = datetime.time(00, 00, 00)
    afternoonDT = datetime.time(12, 00, 00)
    eveningDT = datetime.time(17, 00, 00)

    # if it is  morning give the following responses
    if morningDT < nowDT < afternoonDT:
        if (randomResponse == 1):
            update.message.reply_text('First response')
        if (randomResponse == 2):
            update.message.reply_text('second response')
        if (randomResponse == 3):
            update.message.reply_text('third response')
        if (randomResponse == 4):
            update.message.reply_text('fourth response')
        if (randomResponse == 5):
            update.message.reply_text('fifth response')

    # if it is afternoon give the following responses
    elif afternoonDT < nowDT < eveningDT:
        if (randomResponse == 1):
            update.message.reply_text('First response')
        if (randomResponse == 2):
            update.message.reply_text('second response')
        if (randomResponse == 3):
            update.message.reply_text('third response')
        if (randomResponse == 4):
            update.message.reply_text('fourth response')
        if (randomResponse == 5):
            update.message.reply_text('fifth response')
    # if it is evening give the following responses
    elif nowDT > eveningDT:
        if (randomResponse == 1):
            update.message.reply_text('First response')
        if (randomResponse == 2):
            update.message.reply_text('second response')
        if (randomResponse == 3):
            update.message.reply_text('third response')
        if (randomResponse == 4):
            update.message.reply_text('fourth response')
        if (randomResponse == 5):
            update.message.reply_text('fifth response')
    # if the program cannot determine the time, give a generic response
    else:
        print("Hi, how can I help you today?")



def help_command(update, context):
    update.message.reply_text('If you need help, just ask!')

def error(update, context):
    print(f"update {update} caused error {context.error}")

def main():
    # add and post API
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # additional commands for bot
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    # add error handler
    dp.add_error_handler(error)

    # set polling rate
    updater.start_polling()
    updater.idle()

main()
