'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.db.models import Count
from .models import Market

@admin.register(Market)
# Register your models here.
class MarketsAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ("name","slug","total_products")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_total_products=Count("products"))

    def total_products(self, obj):
        '''Documentation String'''
        return obj._total_products #pylint:disable=w0212

    total_products.short_description = "Total Products"
