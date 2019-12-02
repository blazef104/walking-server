import logging
from telegram.ext import Updater, CommandHandler
from ipgetter2 import IPGetter

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def ip(update, context):
    getter = IPGetter()
    ips=getter.get()
    update.message.reply_text('Your ips:\n v4:{0}\n v6:{1}'.format(ips.v4,ips.v6))

# main

tokenFile = open("token.txt", "r")
token=tokenFile.readline()

updater = Updater(token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('ip', ip))

updater.start_polling()
updater.idle()