from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from customer import models as customer_models


class AddressAdmin(ImportExportModelAdmin):
    list_display = ['user', 'full_name']

class WhislistAdmin(ImportExportModelAdmin):
    list_display = ['user', 'product']

class NotifcationAdmin(ImportExportModelAdmin):
    list_display = ['user', 'type', 'seen', 'date']

admin.site.register(customer_models.Address, AddressAdmin)
admin.site.register(customer_models.Whislist, WhislistAdmin)
admin.site.register(customer_models.Notifications, NotifcationAdmin)
