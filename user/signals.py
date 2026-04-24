'''Signal handlers for the user app.'''
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile
from notification.models import Notification


@receiver(post_save, sender=UserProfile)
def create_welcome_notification(sender, instance, created, **kwargs):
    """Create a default system notification when a user is created.

    This runs whenever a new UserProfile is saved (created=True). It creates
    a `SYSTEM_ALERT` notification letting the user know notifications are
    available.
    """
    if not created:
        return

    try:
        Notification.objects.create(
            user=instance,
            title=Notification.TitleChoices.SYSTEM_ALERT,
            message=(
                "Welcome to Affiliate Partner! Notifications are now enabled "
                "for your account — you'll receive updates about orders, "
                "promotions, and important system alerts here."
            ),
            is_read=False,
        )
    except Exception:
        # Do not raise from the signal; log/report in future as needed.
        pass
# user/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import UserProfile
from notification.models import Notification

@receiver(post_save, sender=UserProfile)
def send_welcome_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance,
            title=Notification.TitleChoices.SYSTEM_ALERT,
            message="Welcome to Affiliate Shop! 🎉"
        )