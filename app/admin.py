from django.contrib import admin
from .models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('Text_chat','Text_date')


admin.site.register(Message, MessageAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('Theme_text','challenge_date','nbr_participants')


admin.site.register(Challenge, ChallengeAdmin)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name_module','question_text','response_text','lien')

admin.site.register(Module,ModuleAdmin)