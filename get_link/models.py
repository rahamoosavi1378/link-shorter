from django.db import models
from django.urls import reverse
import hashlib

# Create your models here.

class Links(models.Model):
    user_input_link = models.URLField(null=False)
    short_link = models.URLField(null=True,blank=True)
    # is_active : default True
    #

    def save(self,*args,**kwargs):
        result_hash = hashlib.md5(self.user_input_link.encode()).hexdigest()
        self.short_link = f'http://127.0.0.1:8000/r/{result_hash}'
        # self.short_link = reverse('get_link_page',args=[result_hashe])
        super().save(*args,**kwargs)

    def __str__(self):
        return self.user_input_link