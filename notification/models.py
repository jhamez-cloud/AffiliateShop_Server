'''Documentation String'''
from django.db import models
from django.utils import timezone

class Notification(models.Model):
    '''Documentation String'''

    class TitleChoices(models.TextChoices):
        '''Documentation String'''
        ORDER_UPDATE = 'ORDER_UPDATE', 'Order Update'
        PROMOTION = 'PROMOTION', 'Promotion'
        SYSTEM_ALERT = 'SYSTEM_ALERT', 'System Alert'

    user = models.ForeignKey(
        "user.UserProfile",
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200, choices=TitleChoices.choices)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification for {self.user.email} - {self.title}" #pylint:disable=e1101
