from django.contrib import admin

from accounts.models import CustomUser, SpecUser

admin.site.register(CustomUser)
admin.site.register(SpecUser)