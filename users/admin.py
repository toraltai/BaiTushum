from django.contrib import admin
from .models import User, ClientUser, SpecUser

admin.site.register(User)
admin.site.register(ClientUser)
admin.site.register(SpecUser)
