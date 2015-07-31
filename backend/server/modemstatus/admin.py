from django.contrib import admin
from modemstatus.models import ModemStatus

class ModemStatusAdmin(admin.ModelAdmin):
    list_display = ('created',)

admin.site.register(ModemStatus, ModemStatusAdmin)

