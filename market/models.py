'''Documentation String'''
from django.db import models

# Create your models here.
class Market(models.Model):
    '''Documentation String'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    @property
    def total_products(self):
        '''Documentation String'''
        return self.products_set.count()

    def __str__(self):
        '''Documentation String'''
        return f"{self.name}"
