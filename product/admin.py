'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Product

@admin.register(Product)
# Register your models here.
class ProductAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("name","slug","image","category","market","link","price","badge")
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ("name","category","market","badge")
    search_fields = ("name","market")
    list_per_page = 10
