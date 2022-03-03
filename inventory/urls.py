from django.urls import path

from .views import ListInventory, ListInventoryView

urlpatterns = [
    path('', ListInventoryView, name='index'),
    path('api/inventory/list', ListInventory.as_view()),
]
