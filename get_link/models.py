from django.db import models

# Create your models here.

class Links(models.Model):
    user_input_link = models.URLField()
    short_link = models.URLField()
