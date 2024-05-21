import telebot
from config.settings import TOKEN

from beebot.models import BotMessage
from beebot.utils import *
from beebot.keyboards import inline_keyboard, menu_keyboard, instruction_keyboard, inline_keyboard_buttons


bot = telebot.TeleBot(TOKEN)


def choose_language_func(message):
    response = BotMessage.objects.get(keyword='choose_language')
    button_text = list(response.buttons.filter(message=response))
    keyboard = inline_keyboard_buttons(text=button_text[0].text, text1=button_text[1].text, next='rus', next1='eng')
    bot.send_message(message.chat.id,
                     text=response.message,
                     reply_markup=keyboard)


def welcome_func(callback):
    response, button_text = get_welcome('welcome_text', callback)
    keyboard = inline_keyboard(text=button_text, next='next')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def menu_func(message):
    language = get_user_language(message.chat.id)  # TODO:
    response, button_text = get_some_messages_and_buttons('menu', language)
    keyboard = menu_keyboard(text1=button_text[0], text2=button_text[1], text3=button_text[2],
        text4=button_text[3], text5=button_text[4])
    bot.send_message(message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def first_step_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('first_step', language)
    keyboard = inline_keyboard(button_text, next='document')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def necessary_documents_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_some_messages_and_buttons('inquired_documents', language)
    keyboard = inline_keyboard_buttons(text=button_text[0], text1=button_text[1], next='certificate', next1='skip')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def help_documents_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_some_messages_and_buttons('help_documents', language)
    keyboard = instruction_keyboard(text1=button_text[0], text2=button_text[1], text3=button_text[2], text4=button_text[3])
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def certificate_of_good_conduct_func(callback):
    language = get_user_language(callback.message.chat.id)
    response = get_message('Справка о несудимости', language)    
    bot.send_message(callback.message.chat.id,text=response)


def medical_insurance_func(callback):
    language = get_user_language(callback.message.chat.id)
    response = get_message('Мед справка', language)    
    bot.send_message(callback.message.chat.id,
                     text=response)


def certificate_from_narcology_func(callback):
    language = get_user_language(callback.message.chat.id)
    response = get_message('Наркология', language)
    bot.send_message(callback.message.chat.id,
                     text=response)


def send_scan_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_some_messages_and_buttons('Отправить HR', language)
    keyboard = inline_keyboard_buttons(text=button_text[0], text1=button_text[1], next='yes', next1='no')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def answer_yes_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('answer yes', language)
    keyboard = inline_keyboard(button_text, 'next1') 
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def answer_no_func(callback):
    language = get_user_language(callback.message.chat.id)
    response = get_message('answer no', language)
    bot.send_message(callback.message.chat.id,
                     text=response)


def mission_and_goal_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Миссия', language)
    keyboard = inline_keyboard(button_text, 'continue')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def company_value_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Ценности', language)
    photo = get_photo('Ценности')
    keyboard = inline_keyboard(button_text, 'next2')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def our_culture_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Привет', language)
    keyboard = inline_keyboard(button_text, 'next3')
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def our_events_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Наши мероприятия', language)
    keyboard = inline_keyboard(button_text, 'next4')
    bot.send_message(callback.message.chat.id,
                   text=response,
                   reply_markup=keyboard)


def family_day_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Family Day', language)
    video = get_video('Family Day')
    keyboard = inline_keyboard(button_text, 'next5') 
    bot.send_video(callback.message.chat.id,
                   video=video,
                   caption=response,
                   reply_markup=keyboard)


def fourteenth_february_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('14 февраля', language)
    video = get_video('14 февраля')
    keyboard = inline_keyboard(button_text, 'next6')
    bot.send_video(
        callback.message.chat.id, video=video,
        caption=response, reply_markup=keyboard
    )


def skylab_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Sky Lab', language)
    photo = get_photo('Sky Lab')
    keyboard = inline_keyboard(button_text, 'next7')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def capsule_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('capsule', language)
    keyboard = inline_keyboard(button_text, 'next8')
    photo = get_photo('capsule')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def location_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('adress', language)
    photo = get_photo('adress')
    keyboard = inline_keyboard(button_text, 'next9')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def kitchen_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Terasse', language)
    photos = get_some_photo('Terasse')
    keyboard = inline_keyboard(button_text, 'next10') 
    bot.send_media_group(callback.message.chat.id,
                    [telebot.types.InputMediaPhoto(photo) for photo in photos])
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def hobby_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('hobby', language)
    photo = get_photo('hobby')
    keyboard = inline_keyboard(button_text, 'next11')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def library_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('library', language)
    photo = get_photo('library')
    keyboard = inline_keyboard(button_text, 'next12')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def bbox_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Bbox', language)
    photo = get_photo('Bbox')
    keyboard = inline_keyboard(button_text, 'next13')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)


def office_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('first_day', language)
    photo = get_photo('first_day')
    keyboard = inline_keyboard(button_text, 'next14')
    bot.send_photo(callback.message.chat.id,
                    photo=photo,
                    caption=response,
                    reply_markup=keyboard)

    
def kitchen_rules_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('rules', language)
    keyboard = inline_keyboard(button_text, 'next15')
    bot.send_message(callback.message.chat.id,
                    text=response,
                    reply_markup=keyboard)


def beestyle_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('Beestyle', language)
    photos = get_some_photo('Beestyle')
    keyboard = inline_keyboard(button_text, 'next16') 
    bot.send_media_group(callback.message.chat.id,
                    [telebot.types.InputMediaPhoto(photo) for photo in photos])
    bot.send_message(callback.message.chat.id,
                     text=response,
                     reply_markup=keyboard)


def first_day_func(callback):
    language = get_user_language(callback.message.chat.id)
    response, button_text = get_message_and_buttons('dont', language)
    keyboard = inline_keyboard(button_text, 'next17')
    bot.send_message(callback.message.chat.id,
                    text=response,
                    reply_markup=keyboard)
