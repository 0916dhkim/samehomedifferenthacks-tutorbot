from Discord import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from assets import messages


# Start button
def start_buttons(bot, update, item, messages):
    fast_search = InlineKeyboardButton(text="fast search")
    help_btn = InlineKeyboardButton(text="help")
    keyboard = [[fast_search, help_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=messages, reply_markup=reply_markup)
    return send

# Button to start serching mentors
def search_mentor_btn(bot, update, item, message):
    search = InlineKeyboardButton(text="search")
    all_mentors = InlineKeyboardButton(text="all mentors")
    close = InlineKeyboardButton(text="close")
    keyboard = [[search], [all_mentors, close]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id, \
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

# Button slide 
def help_slide_btn(bot, update, item, message):
    prev_btn = InlineKeyboardButton(text="prev")
    next_btn = InlineKeyboardButton(text="nxt")
    close = InlineKeyboardButton(text="close")
    keyboard = [[prev_btn, next_btn],[close]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

# Start create question
def start_create_question(bot, update, item, message):
    start = InlineKeyboardButton(text="start")
    keyboard = [[start]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

# Send question
def send_question(bot, update, item, message):
    send = InlineKeyboardButton(text="Send")
    keyboard = [[send]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

# Yet mentors
def slide_mentors(bot, update, item, message):
    button_list = [InlineKeyboardButton("List", callback_data='yet')]
    btn = InlineKeyboardMarkup([button_list])
    return btn
