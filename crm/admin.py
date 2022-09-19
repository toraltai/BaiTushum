from django.contrib import admin
from .models import *


class MusicAdmin(admin.ModelAdmin):
    list_filter = ['is_director']


admin.site.register(Client, MusicAdmin)

admin.site.register(CreditSpecialist)
admin.site.register(Occupation)
admin.site.register(Company)
admin.site.register(Guarantor)
admin.site.register(Property)
admin.site.register(TelephoneConversation)
admin.site.register(MeetConversation)
admin.site.register(DataKK)
admin.site.register(Activity)