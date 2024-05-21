import telebot
import threading

from beebot.bot import *


TOKEN = '6901085243:AAF8AUoXEi2yYDHMYRyqdZUS3Uz6DJy-arA'
bot = telebot.TeleBot(TOKEN)
    

@bot.message_handler(commands=['start'])
def choose_language(message):
    choose_language_func(message)


@bot.callback_query_handler(func=lambda callback: callback.data=='rus' or callback.data=='eng')
def welcome(callback):
    welcome_func(callback)


@bot.message_handler(commands=['menu'])
def menu(message):
    menu_func(message)


@bot.callback_query_handler(func=lambda callback: callback.data=='start')
def welcome_menu(callback):
    welcome_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next' or callback.data=='inquiries')
def first_step(callback):
    first_step_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='document')
def necessary_documents(callback):
    necessary_documents_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='certificate')
def help_documents(callback):
    help_documents_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='good')
def certificate_of_good_conduct(callback):
    certificate_of_good_conduct_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='med')
def medical_insurance(callback):
    medical_insurance_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='narco')
def certificate_from_narcology(callback):
    certificate_from_narcology_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='skip')
def send_scan(callback):
    send_scan_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='yes')
def answer_yes(callback):
    answer_yes_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='no')
def answer_no(callback):
    answer_no_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next1')
def mission_and_goal(callback):
    mission_and_goal_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='continue')
def company_value(callback):
    company_value_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next2')
def our_culture(callback):
    our_culture_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next3' or callback.data=='about_office')
def our_events(callback):
    our_events_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next4')
def family_day(callback):
    family_day_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next5')
def fourteenth_february(callback):
    fourteenth_february_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next6')
def skylab(callback):
    skylab_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next7')
def capsule(callback):
    capsule_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next8')
def location(callback):
    location_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next9')
def kitchen(callback):
    kitchen_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next10')
def hobby(callback):
    hobby_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next11')
def library(callback):
    library_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next12' or callback.data=='bbox')
def bbox(callback):
    bbox_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next13')
def office(callback):
    office_func(callback)

    
@bot.callback_query_handler(func=lambda callback: callback.data=='next14' or callback.data=='rules')
def kitchen_rules(callback):
    kitchen_rules_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next15')
def beestyle(callback):
    beestyle_func(callback)


@bot.callback_query_handler(func=lambda callback: callback.data=='next16')
def first_day(callback):
    first_day_func(callback)


def thread():
    bot.polling(non_stop=True)


def start_polling(*args):
    polling = threading.Thread(target=thread)
    polling.start()
