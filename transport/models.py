from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from django.contrib import admin
from datetime import datetime


class ModelVehicle(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('Model Vehicle')
        verbose_name_plural = _('Model Vehicle')

    def __str__(self):
        return self.name


# Create your models here.
class Vehicle(models.Model):
    license_plates = models.CharField(max_length=200, null=True, verbose_name=_('license plates'))
    model = models.ForeignKey(ModelVehicle, verbose_name=_('model'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')

    def __str__(self):
        return self.license_plates


# Create your models here.
class Driver(models.Model):
    fullname = models.CharField(max_length=200, null=True, verbose_name=_('fullname'))
    phone = models.CharField(max_length=200, null=True, verbose_name=_('phone'))
    identity = models.CharField(max_length=200, null=True, verbose_name=_('identity'))
    address = models.CharField(max_length=200, null=True, verbose_name=_('address'))

    class Meta:
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')

    def __str__(self):
        return self.fullname


class Order(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('order name'))
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='VND', verbose_name=_('price'))
    tax = MoneyField(max_digits=10, decimal_places=2, default_currency='VND', verbose_name=_('tax'))
    salary = MoneyField(max_digits=10, decimal_places=2, default_currency='VND', verbose_name=_('salary'))
    driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL, verbose_name=_('driver'))
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL, verbose_name=_('vehicle'))
    date_started = models.DateTimeField(default=datetime.now(), null=True, verbose_name=_('date started'))
    date_ended = models.DateTimeField(default=datetime.now(), null=True, verbose_name=_('date ended'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

# python manage.py makemessages -l vi
# python manage.py compilemessages
