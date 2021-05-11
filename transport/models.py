from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Vehicle(models.Model):
    license_plates = models.CharField(max_length=200, null=True, verbose_name=_('license plates'))
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    model = models.CharField(max_length=200, null=True, verbose_name=_('model'))

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
    price = models.FloatField(verbose_name=_('price'))
    tax = models.FloatField(verbose_name=_('tax'))
    salary = models.FloatField(verbose_name=_('salary'))
    driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL, verbose_name=_('driver'))
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL, verbose_name=_('vehicle'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

# python manage.py makemessages -l vi
# python manage.py compilemessages