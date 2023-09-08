from django.db import models
from django.urls import reverse


class Links(models.Model):
    user_input_link = models.URLField(null=False)
    hash_link = models.CharField(
        max_length=32,
        null=False,
        db_index=True
    )
    slug = models.SlugField(default='', db_index=True)
    is_active = models.BooleanField(default=True)

    # date: start ~ expire

    def __str__(self):
        return self.user_input_link
