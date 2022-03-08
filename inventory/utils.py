from django.db.models import Q, Sum
from django.db.models.functions import Coalesce

from .models import Inventory


def get_inventory_quantity():
    receiving_quantity = Coalesce(
        Sum('quantity', filter=Q(inventory_type='receiving')), 0)
    shipping_quantity = Coalesce(
        Sum('quantity', filter=Q(inventory_type='shipping')), 0)
    return Inventory.objects \
        .values('commodity') \
        .order_by('commodity') \
        .annotate(quantity=receiving_quantity-shipping_quantity) \
        .values('commodity__name', 'commodity__description', 'quantity')
