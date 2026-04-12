'''Documentation String'''
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from market.models import Market
from category.models import Categorie

# Create your models here.
class Product(models.Model):
    '''Documentation String'''

    class BadgeChoices(models.TextChoices):
        '''Documentation String'''
        HOT = "hot","Hot"
        TOP_PICK = "top pick","Top Pick"
        BEST_SELLER = "best seller","Best Seller"

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="Images/",null=True,blank=True)
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name="categories")
    market = models.ForeignKey(Market,on_delete=models.CASCADE,related_name="products")

    badge = models.CharField(choices=BadgeChoices.choices,default=BadgeChoices.BEST_SELLER)
    rating = models.FloatField(null=True,validators=[MinValueValidator(0),MaxValueValidator(5)],default=1)

    price = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
    original_price = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)


    def __str__(self):
        return f"{self.slug}"
