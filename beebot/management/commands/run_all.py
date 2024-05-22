from django.core.management.base import BaseCommand
from django.core.management import call_command
import threading
from beebot.callbacks import thread


class Command(BaseCommand):
    help = 'Запускает Django сервер и Telegram-бота'

    def handle(self, *args, **options):
        bot_thread = threading.Thread(target=thread)
        bot_thread.daemon = True
        bot_thread.start()
        self.stdout.write(self.style.SUCCESS('Запуск Telegram-бота'))
        call_command('runserver', *args, **options)
