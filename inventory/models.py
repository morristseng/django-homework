from django.conf import settings
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)


class TradeParner(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Commodity(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    customer = models.ForeignKey(TradeParner, on_delete=models.CASCADE)


class Inventory(models.Model):
    customer = models.ForeignKey(TradeParner, on_delete=models.CASCADE)
    InventoryType = models.TextChoices('InventoryType', 'shipping receiving')
    inventory_type = models.CharField(
        choices=InventoryType.choices, max_length=9)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class InventoryLog(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action_choices = models.TextChoices('ActionChoice', 'add modify delete')
    action_type = models.CharField(
        choices=action_choices.choices, max_length=6)
    details = models.CharField(max_length=2048)
    timestamp = models.DateTimeField(auto_now_add=True)
