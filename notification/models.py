'''Documentation String'''
from django.db import models

# Create your models here.
class Notification(models.Model):
    '''Documentation String'''
    title = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title}"
