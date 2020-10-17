from django.contrib import admin
from .models import Conversation, ConversationMessage

admin.site.register(Conversation)

@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'created_by']
