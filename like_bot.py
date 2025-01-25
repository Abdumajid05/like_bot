import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = os.environ['TOKEN']

button_count = {'like': 0, 'dislike': 0}
result = {}

def button_callback(update: Update, context):
    query = update.callback_query
    user_id = query.from_user.id

    l_d_count = result.get(user_id, None)

    if query.data == 'like':
        if l_d_count == 'dislike':
            button_count['dislike'] -= 1
        if l_d_count != 'like':
            button_count['like'] += 1
            result[user_id] = 'like'

    elif query.data == 'dislike':
        if l_d_count == 'like':
            button_count['like'] -= 1
        if l_d_count != 'dislike':
            button_count['dislike'] += 1
            result[user_id] = 'dislike'

    inline_button = InlineKeyboardButton(text=f"👍 {button_count['like']}", callback_data='like')
    inline_button1 = InlineKeyboardButton(text=f"👎 {button_count['dislike']}", callback_data='dislike')
    inline_keyboard = InlineKeyboardMarkup([[inline_button, inline_button1]])

    query.edit_message_reply_markup(reply_markup=inline_keyboard)

def like(update: Update, context):
    photo = update.message.photo[-1]
    file_id = photo.file_id

    inline_button = InlineKeyboardButton(text=f"👍 {button_count['like']}", callback_data='like')
    inline_button1 = InlineKeyboardButton(text=f"👎 {button_count['dislike']}", callback_data='dislike')
    inline_keyboard = InlineKeyboardMarkup([[inline_button, inline_button1]])

    update.message.reply_photo(photo=file_id, caption="Like va dislike tugmalarini bosing", reply_markup=inline_keyboard)

def start(update: Update, context):
    update.message.reply_text("Hello")

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.photo, like))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(button_callback))

updater.start_polling()
updater.idle()