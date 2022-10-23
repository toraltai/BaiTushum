from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'credit_type', 'id_credit_spec']
    list_filter = ['credit_type']
    search_fields = ['id', 'full_name']


admin.site.register(Client, ClientAdmin)
admin.site.register(Entity)
admin.site.register(Company)
admin.site.register(Guarantor)
admin.site.register(Files)


class FileInAdmin(admin.TabularInline):
    model = Files
    fields = ['file']
    max_num = 5


class ImageInAdmin(admin.TabularInline):
    model = Images
    fields = ['image']
    max_num = 5


class PropertyAdmin(admin.ModelAdmin):
    inlines = [FileInAdmin, ImageInAdmin]
    list_display = ['images']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Conversation)
admin.site.register(DataKK)
admin.site.register(Activity)
admin.site.register(Images)
