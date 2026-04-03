from django.contrib import admin
from .models import Message, Announcement

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('subject', 'sender__username', 'recipient__username')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_important')
    list_filter = ('is_important', 'created_at')
    search_fields = ('title', 'author__username')
