from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Inventory, InventoryLog


@receiver(post_save, sender=Inventory)
def log_inventory_change(sender, **kwargs):
    obj = kwargs["instance"]
    updated = kwargs["update_fields"]
    action_type = 'add' if kwargs['created'] else 'modify'
    if action_type == 'add':
        details = f"{obj.id} is created"
    elif action_type == 'modify':
        details = (
            f"{obj.id}'s field: {','.join(updated)} "
            f"{'are' if len(updated) > 1 else 'is'} changed"
        )
    InventoryLog.objects.create(
        who=obj.user,
        action_type=action_type,
        details=details,
    )


@receiver(post_delete, sender=Inventory)
def log_inventory_delete(sender, **kwargs):
    obj = kwargs["instance"]
    InventoryLog.objects.create(
        who=obj.user,
        action_type='delete',
        details=f"{obj.id} is deleted.",
    )
