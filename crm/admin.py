from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Entity)
admin.site.register(CreditSpecialist)
admin.site.register(Occupation)
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


admin.site.register(Property, PropertyAdmin)
admin.site.register(TelephoneConversation)
admin.site.register(MeetConversation)
admin.site.register(DataKK)
admin.site.register(Activity)
admin.site.register(Images)
