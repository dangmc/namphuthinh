from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    vehicles = Vehicle.objects.all()
    orders = Order.objects.all()
    drivers = Driver.objects.all()
    total_vehicles = vehicles.count()
    total_orders = orders.count()
    total_drivers = drivers.count()

    context = {
        "vehicles": vehicles,
        "orders": orders,
        "drivers": drivers,
        "total_vehicles": total_vehicles,
        "total_orders": total_orders,
        "total_drivers": total_drivers,
    }
    return render(request, 'transport/dashboard.html', context)


def vehicle(request):
    vehicle_items = Vehicle.objects.all()
    return render(request, 'transport/vehicle.html', {'vehicles': vehicle_items})


def driver(request):
    driver_items = Driver.objects.all()
    return render(request, 'transport/driver.html', {'drivers': driver_items})
