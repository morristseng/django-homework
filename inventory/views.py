from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Inventory
from .serializers import InventorySerializer


def ListInventoryView(request):
    return render(request, 'inventory/index.html')

class ListInventory(APIView):
    def get(self, request):
        page = int(request.GET.get('page', '1'))
        offset = int(request.GET.get('o', '50'))
        queryset = Inventory.objects.all()
        # Question:
        # Why not just use pagination from django rest framework?
        # https://www.django-rest-framework.org/api-guide/pagination/
        p = Paginator(queryset, offset)
        cur_page = p.page(page)
        serializer = InventorySerializer(cur_page.object_list, many=True)
        return Response({
            "count": p.count,
            "results": serializer.data,
        })
