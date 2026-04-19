'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("firebase_uid","email")
