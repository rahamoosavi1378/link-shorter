from django.contrib import admin
from . import models


# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ['user_input_link', 'hash_link', 'slug', 'is_active']


admin.site.register(models.Links, LinksAdmin)
