'''Documentation String'''
from rest_framework import serializers
from .models import Categorie

class CategorySerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = Categorie
        fields = "__all__"