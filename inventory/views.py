from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Inventory
from .serializers import InventorySerializer, InventoryStatusSerializer


def list_inventory(request):
    return render(request, 'inventory/index.html')


def list_inventory_status(request):
    return render(request, 'inventory/status.html')


def paginator_helper(request, queryset):
    page_num = int(request.GET.get('page', '1'))
    page_size = int(request.GET.get('o', '50'))
    paginator = Paginator(queryset, page_size)
    return paginator.page(page_num), paginator.count


@api_view(['GET'])
def list_inventory_api(request):
    queryset = Inventory.objects \
        .select_related('customer', 'commodity').all().order_by('id')
    cur_page, count = paginator_helper(request, queryset)
    serializer = InventorySerializer(cur_page.object_list, many=True)
    return Response({
        "count": count,
        "results": serializer.data,
    })


@api_view(['GET'])
def list_inventory_status_api(request):
    receiving_quantity = Coalesce(
        Sum('quantity', filter=Q(inventory_type='receiving')), 0)
    shipping_quantity = Coalesce(
        Sum('quantity', filter=Q(inventory_type='shipping')), 0)
    queryset = Inventory.objects \
        .values('commodity') \
        .order_by('commodity') \
        .annotate(quantity=receiving_quantity-shipping_quantity) \
        .values('commodity__name', 'commodity__description', 'quantity')
    cur_page, count = paginator_helper(request, queryset)
    serializer = InventoryStatusSerializer(cur_page.object_list, many=True)
    return Response({
        "count": count,
        "results": serializer.data,
    })
