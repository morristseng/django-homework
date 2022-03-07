from django.contrib import admin

from inventory.models import Commodity, Inventory, TradeParner, User


# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save(update_fields=form.changed_data if change else None)

    def delete_model(self, request, obj):
        obj.user = request.user
        super().delete_model(request, obj)


admin.site.register(User)
admin.site.register(TradeParner)
admin.site.register(Commodity)
admin.site.register(Inventory, InventoryAdmin)
