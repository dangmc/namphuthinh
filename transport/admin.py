from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'license_plates', 'model', 'date_register')
    ordering = ['license_plates']
    search_fields = ['license_plates']
    list_per_page = 20


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'identity', 'phone', 'address')
    ordering = ['id']
    search_fields = ['fullname', 'identity', 'phone']
    list_per_page = 20

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            print("driver size ", len(csv_data))
            for x in csv_data:
                fields = x.split(",")
                created = Driver.objects.update_or_create(
                    fullname=fields[0],
                    phone=fields[1],
                    identity=fields[2],
                    address=fields[3]
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['driver', 'vehicle']
    list_display = ('id', 'name', 'driver', 'vehicle', 'expense', 'revenue', 'date_started', 'date_ended')
    list_display_links = ['driver']
    search_fields = ['driver__fullname', 'vehicle__license_plates']
    list_filter = ['date_started', 'date_ended']
    actions = ['download_csv']
    list_per_page = 20

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
