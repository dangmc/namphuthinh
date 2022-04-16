from io import BytesIO

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
        import pandas as pd
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            data = pd.read_excel(csv_file, sheet_name='driver')
            headers = ['tên', 'sdt', 'cmt', 'địa chỉ']
            cols = data.columns.ravel()
            for i in range(len(headers)):
                if headers[i] != cols[i].lower():
                    messages.warning(request, 'Sai tên trường')
                    return HttpResponseRedirect(request.path_info)
            csv_data = data.values.tolist()
            for x in csv_data:
                created = Driver.objects.update_or_create(
                    fullname=x[0],
                    phone=x[1],
                    identity=x[2],
                    address=x[3]
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
        from django.http import HttpResponse
        import pandas as pd
        with BytesIO() as b:
            data = [[order.name, order.driver.fullname, order.vehicle.license_plates,
                     order.date_started.strftime("%m/%d/%Y, %H:%M:%S"), order.date_ended.strftime("%m/%d/%Y, %H:%M:%S"),
                     order.revenue, order.expense] for order in queryset]
            df = pd.DataFrame(data, columns=["Tên chuyến", "Tài xế", "Biển số xe", "Ngày đi", "Ngày về", "Doanh thu",
                                             "Chi phí"])
            with pd.ExcelWriter(b) as writer:
                df.to_excel(writer, sheet_name="orders", index=False)

            filename = f"orders.xlsx"
            res = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            res['Content-Disposition'] = f'attachment; filename={filename}'
            return res

    download_csv.short_description = _('download selected items')


admin.site.register(ModelVehicle)
