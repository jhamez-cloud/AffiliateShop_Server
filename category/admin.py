'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Categorie

@admin.register(Categorie)
# Register your models here.
class CategorieAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("name","slug")
