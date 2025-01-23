import os
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
TOKEN = os.environ['TOKEN']  

like = 0
dislike = 0
def like_handler(update: Update, context):
    global like, dislike 
    if update.message.text == '👍':
        like += 1
    elif update.message.text == '👎':
        dislike += 1
    update.message.reply_text(f"Likes: {like}\nDislikes: {dislike}")


updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, like_handler))
updater.start_polling()
updater.idle()
