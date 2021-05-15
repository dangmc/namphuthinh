from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('driver/', views.driver, name='driver'),
]
