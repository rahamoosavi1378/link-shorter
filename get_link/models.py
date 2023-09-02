from django.db import models
from django.urls import reverse


# import hashlib


# Create your models here.

class Links(models.Model):
    user_input_link = models.URLField(null=False)
    hash_link = models.CharField(max_length=32,
                                 null=False,
                                 db_index=True)
    is_active = models.BooleanField(default=True)

    # date: start ~ expire

    # def save(self, *args, **kwargs):
    #     self.hash_link = hashlib.md5(self.user_input_link.encode()).hexdigest()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.user_input_link
