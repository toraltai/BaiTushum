from django.contrib import admin

# class UserAdmin(admin.ModelAdmin):
#     list_filter = ['is_staff']
#     search_fields = ['username']
#
#
# admin.site.register(User, UserAdmin)
# =======
from .models import User, ClientUser, SpecUser

admin.site.register(User)
admin.site.register(ClientUser)
admin.site.register(SpecUser)
