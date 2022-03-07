from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_inventory, name='index'),
    path('status', views.list_inventory_status),
    path('log', views.list_inventory_log),
]
