from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Links

# pre_save signal using decorator

def set_hash_link(sender,instance,**kwargs):
    pass

