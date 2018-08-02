#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram.ext as telegram
import logging
import random #para números al azar

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

###########    funciones y otras cosas mías
def dado20(x):
    x = random.randint(1, 20) #int al azar entre 1 y 20
    return x

x = 0

#poo = telegram.Emoji.PILE_OF_POO #emoji de popó
poo = 'no hay popo'

ayuda = '''
Hola!
Esta ayuda no será de mucha ayuda, lo siento...
Mi bot no hace nada más que repetir lo que dices.
(lo sé, es molesto)

Algunos comandos:
/dado tira 1d20
/popo pues... popó
/pito no sé!
/help la quesque ayuda
/start no inicia, solo saluda
cualquier cosa, escribeme: telegram.me/eliand
'''

#############


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hola guapo!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text=ayuda)
    
def dado(bot, update):
    bot.sendMessage(update.message.chat_id, text=dado20(x) )

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def popo(bot, update):
    bot.sendMessage(update.message.chat_id, text=poo)

def pito(bot, update):
    bot.sendMessage(update.message.chat_id, text='pues güevos para ti, pendejo')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.

    TOKEN = os.environ.get('TOKEN')
    updater = Updater(TOKEN) #aquí va el token

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dado", dado))
    dp.add_handler(CommandHandler("popo", popo))
    dp.add_handler(CommandHandler("pito", pito))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_handler(ErrorHandler(error))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
