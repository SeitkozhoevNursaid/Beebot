from django.contrib import admin
from django.http import HttpRequest
from beebot.models import BotMessage, BotPhoto, BotVideo, BotToken, BotButtons, BotUser
from beebot.forms import BotTokenForm
from django.contrib.auth.models import Group
from beebot.callbacks import start_polling


class BotVideoInline(admin.TabularInline):
    model = BotVideo
    extra = 1
    max_num = 2


class BotPhotoInline(admin.TabularInline):
    model = BotPhoto
    extra = 1
    max_num = 2


class BotButtonsInline(admin.TabularInline):
    model = BotButtons
    extra = 1


@admin.register(BotToken)
class BotTokenAdmin(admin.ModelAdmin):
    form = BotTokenForm

    def start_bot_polling(self, request, queryset):
        for token in queryset:
            start_polling(token.token)

    start_bot_polling.short_description = "Запустить бота"

    actions = [start_bot_polling]


@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    inlines = [BotPhotoInline, BotVideoInline, BotButtonsInline]
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    exclude = ['keyword']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(BotPhoto)
class BotPhotoAdmin(admin.ModelAdmin):
    list_display = ("message",)
    list_filter = ("message",)
    search_fields = ("message",)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(BotVideo)
class BotVideoAdmin(admin.ModelAdmin):
    list_display = ("message",)
    list_filter = ("message",)
    search_fields = ("message",)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(BotButtons)
class BotButtonsAdmin(admin.ModelAdmin):
    list_display = ("message",)
    list_filter = ("message",)
    search_fields = ("message",)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(BotUser)
admin.site.unregister(Group)
