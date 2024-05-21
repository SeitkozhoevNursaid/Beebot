from beebot.models import BotVideo, BotMessage, BotPhoto, BotUser


def save_language_preference(chat_id, language):
    username = str(chat_id)
    profile, created = BotUser.objects.get_or_create(username=username)
    profile.language = language
    profile.save(update_fields=['language'])


def get_user_language(chat_id):
    profile = BotUser.objects.get(username=chat_id)
    return profile.language


def get_message_and_buttons(message_name, language):
    message_object = BotMessage.objects.get(keyword=message_name)
    button = message_object.buttons.get(message=message_object)
    if language == 'rus':
        response = message_object.message
        button_text = button.text
    else:
        response = message_object.message_eng
        button_text = button.text_eng
    return response, button_text


def get_video(message_name):
    message_object = BotMessage.objects.get(keyword=message_name)
    video_object = BotVideo.objects.get(message=message_object)
    video = open(file=f'media/{str(video_object.video)}', mode='rb')    
    return video


def get_photo(message_name):
    message_object = BotMessage.objects.get(keyword=message_name)
    photo_object = BotPhoto.objects.get(message=message_object)
    photo = open(file=f'media/{str(photo_object.image)}', mode='rb')
    return photo


def get_some_messages_and_buttons(message_name, language):
    message_object = BotMessage.objects.get(keyword=message_name)
    button = list(message_object.buttons.filter(message=message_object).values_list('text', 'text_eng'))
    if language == 'rus':
        response = message_object.message
        button_text = [i[0] for i in button]
    else:
        response = message_object.message_eng
        button_text = [i[1] for i in button]
    return response, button_text


def get_message(message_name, language):
    message_object = BotMessage.objects.get(keyword=message_name)
    if language == 'rus':
        response = message_object.message
    else:
        response = message_object.message_eng
    return response


def get_some_photo(message_name):
    message_object = BotMessage.objects.get(keyword=message_name)
    photo_objects = list(BotPhoto.objects.filter(message=message_object))
    photos = [open(file=f'media/{str(i.image)}', mode='rb') for i in photo_objects]
    return photos


def get_welcome(message_name, callback):
    message_object = BotMessage.objects.get(keyword=message_name)
    button = message_object.buttons.get(message=message_object)
    if callback.data == 'rus':
        response = message_object.message
        button_text = button.text
        save_language_preference(callback.message.chat.id, 'rus')
    else:
        response = message_object.message_eng
        button_text = button.text_eng
        save_language_preference(callback.message.chat.id, 'eng')
    return response, button_text
