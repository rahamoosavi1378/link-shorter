from django.db import models

# Create your models here.

class Links(models.Model):
    user_input_link = models.URLField(verbose_name='لینک ورودی کاربر')
    short_link = models.URLField(verbose_name='لینک ورودی کاربر')
