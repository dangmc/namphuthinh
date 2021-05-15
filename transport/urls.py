from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('driver/', views.driver, name='driver'),
    path('manager/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='manager'),
]
