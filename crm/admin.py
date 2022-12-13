from django.contrib import admin
from .models import *
from jet.admin import CompactInline


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'credit_type', 'id_credit_spec']
    list_filter = ['credit_type']
    search_fields = ['id', 'full_name']


admin.site.register(Client, ClientAdmin)


class EntityAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name_director', 'client_company', 'id_credit_spec']
    search_fields = ['id', 'full_name_director']


admin.site.register(Entity, EntityAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'legal_address', ]
    list_filter = ['field_activity']
    search_fields = ['id', 'company_name']


admin.site.register(Company, CompanyAdmin)


class GuarantorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'address']
    search_fields = ['id', 'full_name']


admin.site.register(Guarantor, GuarantorAdmin)


# admin.site.register(Files)
# admin.site.register(Client)
# admin.site.register(Entity)
# admin.site.register(Company)
# admin.site.register(Guarantor)
# admin.site.register(Files)


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
    list_display = ['id', 'type', ]
    search_fields = ['id', 'type', ]


admin.site.register(Property, PropertyAdmin)


class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_filter = ['date', 'is_meeting']
    search_fields = ['id', 'name', 'date']


admin.site.register(Conversation, ConversationAdmin)


class DataKKAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date']
    search_fields = ['id', 'created_date']


admin.site.register(DataKK, DataKKAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'activites_add']
    search_fields = ['id', 'activites_add']


admin.site.register(Activity, ActivityAdmin)