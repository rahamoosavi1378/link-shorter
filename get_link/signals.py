from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Links

# import hashlib
from utils.hasher import MD5,GenSlug

# pre_save signal using decorator

@receiver(pre_save, sender=Links)
def set_hash_link(sender, instance, **kwargs):
    instance.hash_link = MD5(instance.user_input_link).md5()
    instance.slug = GenSlug()
