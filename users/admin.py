from django.contrib import admin
from .models import User, SpecUser


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__','full_name', 'phone_number']

# admin.site.register(ClientUser)

# admin.site.register(SpecUser)
@admin.register(SpecUser)
class SpecUserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']