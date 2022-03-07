from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list_inventory_api, name='list'),
    path('status', views.list_inventory_status_api, name='status'),
    path('log', views.list_inventory_log_api),
]
