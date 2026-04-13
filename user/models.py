'''Documentation String'''
from django.db import models
from notification.models import Notification

# Create your models here.
class User(models.Model):
    '''Documentation String'''
    firebase_uid = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    notification = models.ForeignKey(Notification,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} - {self.firebase_uid}"
