from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Commodity, Inventory, InventoryLog, TradeParner


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeParner
        fields = ('name', 'address')


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = ('name', 'description')


class InventorySerializer(serializers.ModelSerializer):
    customer = CompanySerializer(read_only=True)
    commodity = CommoditySerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ('id', 'inventory_type', 'quantity', 'customer', 'commodity')


class InventoryStatusSerializer(serializers.Serializer):
    commodity__name = serializers.CharField()
    commodity__description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        fields = ('commodity__name', 'commodity__description', 'quantity')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)


class InventoryLogSerializer(serializers.ModelSerializer):
    who = UserSerializer(read_only=True)

    class Meta:
        model = InventoryLog
        fields = ('who', 'action_type', 'details', 'timestamp')
