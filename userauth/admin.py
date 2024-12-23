from django.contrib import admin
from userauth import models

admin.site.register(models.User)
admin.site.register(models.Profile)
