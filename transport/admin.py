from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plates', 'model', 'date_register')
    ordering = ['license_plates']
    search_fields = ['license_plates']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'identity', 'phone', 'address')
    ordering = ['fullname']
    search_fields = ['fullname', 'identity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['driver', 'vehicle']
    list_display = ('name', 'driver', 'vehicle', 'expense', 'revenue', 'date_started', 'date_ended')
    search_fields = ['driver__fullname', 'vehicle__license_plates']

    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        f = open('some.csv', 'w', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(["name", "driver"])

        for order in queryset:
            writer.writerow([order.name, order.driver.fullname])

        f.close()

        f = open('some.csv', 'r', encoding='utf-8')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

    download_csv.short_description = _('download selected items')


admin.site.register(ModelVehicle)
