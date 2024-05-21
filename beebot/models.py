from django.db import models
from django.contrib.auth.models import AbstractUser


class BotMessage(models.Model):
    name = models.CharField(("Ключевое название сообщения"), max_length=100)
    message = models.TextField(("Сообщение бота на Русском"))
    message_eng = models.TextField(('Соощение бота на Кыргызском'))
    keyword = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Сообщение бота'
        verbose_name_plural = 'Сообщении бота'

    def __str__(self):
        return self.name


class BotVideo(models.Model):
    video = models.FileField(("Видео"), upload_to='videos/', max_length=100, null=True, blank=True)
    message = models.ForeignKey(BotMessage, verbose_name=("Сообщение к которому прикреплено видео"), on_delete=models.CASCADE, related_name='video')

    class Meta:
        verbose_name = 'Видео которое прикрепите к боту'
        verbose_name_plural = 'Видео которые прикреплены к боту'
        
    def __str__(self):
        return str(self.message)


class BotPhoto(models.Model):
    image = models.ImageField(("Фото"), upload_to='images/', null=True, blank=True)
    message = models.ForeignKey(BotMessage, verbose_name=("Сообщение к которому прикреплено фото"), on_delete=models.CASCADE, related_name='photo')

    class Meta:
        verbose_name = 'Фото которое прикрепите к боту'
        verbose_name_plural = 'Фотки которые прикреплены к боту'

    def __str__(self):
        return str(self.message)


class BotToken(models.Model):
    token = models.CharField(('Токен'), max_length=100)

    class Meta:
        verbose_name = 'Запуск бота'
        verbose_name_plural = 'Запуск бота'

    def __str__(self):
        return self.token


class BotButtons(models.Model):
    text = models.CharField(("Текст кнопки на Русском"), max_length=50)
    text_eng = models.CharField(('Текст кнопки на Кыргызском'), max_length=50)
    message = models.ForeignKey(
        BotMessage, verbose_name=("Сообщение к которому эта кнопка"), 
        related_name='buttons', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Текст кнопки'
        verbose_name_plural = 'Текста кнопок'

    def __str__(self):
        return str(self.message)


class BotUser(AbstractUser):
    language = models.CharField(max_length=10, verbose_name='Язык', choices=[('rus', 'Russian'), ('kg', 'Kyrgyz')])
