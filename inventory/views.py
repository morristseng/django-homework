from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Inventory, InventoryLog
from .serializers import (InventoryLogSerializer, InventorySerializer,
                          InventoryStatusSerializer)
from .utils import get_inventory_quantity


def list_inventory(request):
    return render(request, 'inventory/index.html')


def list_inventory_status(request):
    return render(request, 'inventory/status.html')

def list_inventory_log(request):
    return render(request, 'inventory/log.html')


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
    cur_page, count = paginator_helper(request, get_inventory_quantity())
    serializer = InventoryStatusSerializer(cur_page.object_list, many=True)
    return Response({
        "count": count,
        "results": serializer.data,
    })


@api_view(['GET'])
def list_inventory_log_api(request):
    queryset = InventoryLog.objects.select_related('who').all().order_by('id')
    cur_page, count = paginator_helper(request, queryset)
    serializer = InventoryLogSerializer(cur_page.object_list, many=True)
    return Response({
        "count": count,
        "results": serializer.data,
    })
