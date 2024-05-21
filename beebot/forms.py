from django import forms

from beebot.models import BotVideo, BotPhoto, BotToken, BotButtons


class BotPhotoForm(forms.ModelForm):

    class Meta:
        model = BotPhoto
        fields = ['image']
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'miltiple': True})
        }


class BotVideoForm(forms.ModelForm):

    class Meta:
        model = BotVideo
        fields = ['video']
        widgets = {
            'video' : forms.ClearableFileInput(attrs={'miltiple': True})
        }


class BotButtonsForm(forms.ModelForm):

    class Meta:
        model = BotButtons
        fields = ['text']
        widgets = {
            'text' : forms.ClearableFileInput(attrs={'miltiple': True})
        }


class BotTokenForm(forms.ModelForm):
    class Meta:
        model = BotToken
        fields = ['name']
