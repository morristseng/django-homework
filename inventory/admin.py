from django.contrib import admin
from inventory.models import User, TradeParner, Commodity, Inventory

# Register your models here.
admin.site.register(User)
admin.site.register(TradeParner)
admin.site.register(Commodity)
admin.site.register(Inventory)