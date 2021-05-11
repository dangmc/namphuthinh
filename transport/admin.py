from django.contrib import admin
from .models import *


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_plates', 'model',)
    ordering = ['name']
    search_fields = ['license_plates']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'identity', 'phone', 'address')
    ordering = ['fullname']
    search_fields = ['fullname', 'identity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['driver', 'vehicle']
    list_display = ('name', 'driver', 'vehicle', 'price', 'tax', 'salary')
