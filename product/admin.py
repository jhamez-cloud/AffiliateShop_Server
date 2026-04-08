'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Product

@admin.register(Product)
# Register your models here.
class ProductAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("name","slug","category","market","link")
    list_filter = ("name","category","market")
    search_fields = ("name","market")
    list_per_page = 10
