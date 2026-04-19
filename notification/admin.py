'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Notification

# Register your models here.
@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("user", "title", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("user__email", "title", "message")
    readonly_fields = ("created_at",)
