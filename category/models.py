'''Documentation String'''
from django.db import models

# Create your models here.
class Categorie(models.Model):
    '''Documentation String'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        '''Documentation String'''
        return f"{self.name}"
