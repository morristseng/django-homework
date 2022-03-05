from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_inventory, name='index'),
    path('status', views.list_inventory_status),
    path('log', views.list_inventory_log),
    path('api/inventory/list', views.list_inventory_api, name='list'),
    path(
        'api/inventory/status',
        views.list_inventory_status_api,
        name='status',
    ),
    path('api/inventory/log', views.list_inventory_log_api),
]
