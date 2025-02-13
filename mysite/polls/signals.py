from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from polls.models import Profile,Like,Watchlist

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)
        Like.objects.create(user=instance)
        Watchlist.objects.create(user=instance)