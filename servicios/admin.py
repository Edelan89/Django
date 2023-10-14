from django.contrib import admin

# Register your models here.

from .models import Servicios

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicios, ServicioAdmin)