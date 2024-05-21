import telebot


def inline_keyboard(text, next):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text=text, callback_data=next)
    keyboard.add(button)
    return keyboard


def inline_keyboard_buttons(text, next, text1, next1):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text=text, callback_data=next)
    button2 = telebot.types.InlineKeyboardButton(text=text1, callback_data=next1)
    keyboard.add(button, button2)
    return keyboard


def menu_keyboard(text1, text2, text3, text4, text5):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)
    button1 = telebot.types.InlineKeyboardButton(text=text1, callback_data='start')
    button2 = telebot.types.InlineKeyboardButton(text=text2, callback_data='inquiries')
    button3 = telebot.types.InlineKeyboardButton(text=text3, callback_data='rules')
    button4 = telebot.types.InlineKeyboardButton(text=text4, callback_data='about_office')
    button5 = telebot.types.InlineKeyboardButton(text=text5, callback_data='bbox')
    keyboard.row(button1, button2, button3)
    keyboard.row(button4, button5)
    return keyboard


def instruction_keyboard(text1, text2, text3, text4):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text=text1, callback_data='good')
    button2 = telebot.types.InlineKeyboardButton(text=text2, callback_data='med')
    button3 = telebot.types.InlineKeyboardButton(text=text3, callback_data='narco')
    button4 = telebot.types.InlineKeyboardButton(text=text4, callback_data='skip')
    keyboard.row(button1, button2, button3)
    keyboard.row(button4)
    return keyboard
