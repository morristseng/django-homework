from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_inventory, name='index'),
    path('status', views.list_inventory_status),
    path('api/inventory/list', views.list_inventory_api, name='list'),
    path(
        'api/inventory/status',
        views.list_inventory_status_api,
        name='status',
    ),
]
