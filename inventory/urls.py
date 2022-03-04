from django.urls import path

from .views import (ListInventory, ListInventoryStatus,
                    ListInventoryStatusView, ListInventoryView)

urlpatterns = [
    path('', ListInventoryView, name='index'),
    path('status', ListInventoryStatusView),
    path('api/inventory/list', ListInventory.as_view(), name='list'),
    path('api/inventory/status', ListInventoryStatus.as_view(), name='status'),
]
