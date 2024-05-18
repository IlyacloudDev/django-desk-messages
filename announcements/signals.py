from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Author


@receiver(post_save, sender=User)
def user_created(instance, **kwargs):
    author = Author.objects.create(author_name=instance.id)
