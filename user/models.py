'''Documentation String'''
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    '''Documentation String'''
    firebase_uid = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    fullname = models.CharField(max_length=100,blank=True,null=True)
    #last_name = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        '''Documentation String'''
        return True
    @property
    def is_anonymous(self):
        '''Documentation String'''
        return False

    def __str__(self):
        return f"{self.email} - {self.firebase_uid}"
