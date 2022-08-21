from telegram.ext.updater import Updater
from telegram.update import Update
from telegram import Bot
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, Handler
import os
import spotdl
import logging





token="5651347287:AAGjSHeR5J1Z-oIf9Ohb9ROvy-UAjgO1z9E"


updater = Updater(token,use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text("hello nice to meet you         سلام علیکم ")




def send_song(update, context):

	logging.log(logging.ERROR, 'you should select one of downloaders')
	url= "" +update.message.text + ""
	os.system(f'mkdir -p .temp{url}')
	os.chdir(f'./.temp{url}')
	update.message.reply_text("searching ....")
	try:
		os.system(f'spotdl {url}')
		
	except:
		pass


	
	#os.chdir('./..')
	#os.system(f'rm -rf .temp{url}')



def main():
	token="5651347287:AAGjSHeR5J1Z-oIf9Ohb9ROvy-UAjgO1z9E"
	updater = Updater(token, use_context=True)
	dispatcher = updater.dispatcher
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(MessageHandler(Filters.text, send_song))


	updater.start_polling()
	updater.idle()
main()
