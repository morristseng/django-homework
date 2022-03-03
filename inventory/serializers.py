from rest_framework import serializers

from . import models


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = ('inventory_type', 'quantity', 'customer', 'commodity')
