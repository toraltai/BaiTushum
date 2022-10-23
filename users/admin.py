from django.contrib import admin
# from .models import User, ClientUser, SpecUser
from django.contrib.auth.models import Group
#
admin.site.unregister(Group)
# admin.site.register(User)
# admin.site.register(ClientUser)
# admin.site.register(SpecUser)
