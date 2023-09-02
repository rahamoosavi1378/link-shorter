from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Links

import hashlib


# pre_save signal using decorator

@receiver(pre_save, sender=Links)
def set_hash_link(sender, instance, **kwargs):
    instance.hash_link = hashlib.md5(
        instance.user_input_link.encode()).hexdigest()
