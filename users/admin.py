from django.contrib import admin
from .models import User, ClientUser, SpecUser


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__','full_name', 'phone_number']

# admin.site.register(ClientUser)
@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = ['__str__']

# admin.site.register(SpecUser)
@admin.register(SpecUser)
class SpecUserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']