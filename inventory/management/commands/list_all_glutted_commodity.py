from django.core.management.base import BaseCommand
from inventory.utils import get_inventory_quantity
from prettytable import PrettyTable


class Command(BaseCommand):
    help = 'Show the commodity that greater equal than specific number (default: 100).'

    def add_arguments(self, parser):
        parser.add_argument('--quantity', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        queryset = get_inventory_quantity()
        queryset.filter(quantity__gte=options["quantity"])
        result = list(queryset.filter(quantity__gte=options["quantity"]))
        x = PrettyTable()
        x.field_names = ['Commodity Name', 'Commodity Desc', 'Quantity']
        x.add_rows([
            [
                row['commodity__name'],
                row['commodity__description'],
                row['quantity'],
            ] for row in result
        ])
        print(x)
