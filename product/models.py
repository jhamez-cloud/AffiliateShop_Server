'''Documentation String'''
from django.db import models
from market.models import Market
from category.models import Categorie

# Create your models here.
class Product(models.Model):
    '''Documentation String'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    link = models.URLField(max_length=200)
    #image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    market = models.ForeignKey(Market,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.slug}"
