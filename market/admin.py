'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Market

@admin.register(Market)
# Register your models here.
class MarketsAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("name","slug",)
