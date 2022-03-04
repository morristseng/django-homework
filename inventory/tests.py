from django.test import TestCase
from django.urls import reverse

from .models import Commodity, Inventory, TradeParner


def create_basic():
    parner = TradeParner.objects.create(name='parner1', address='add1')
    commodity1 = Commodity.objects.create(name='Switch', description='Switch OLED', customer=parner)
    commodity2 = Commodity.objects.create(name='PS5', description='PS5', customer=parner)
    return parner, commodity1, commodity2

class ListInventoryStatusTests(TestCase):
    def test_receiving_quantity(self):
        parner, commodity, _ = create_basic()
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity, quantity=50)
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity, quantity=4)
        response = self.client.get(reverse('status'))
        object = response.json()
        self.assertEqual(object["count"], 1)
        self.assertEqual(object["results"][0]["quantity"], 54)

    def test_shipping_quantity(self):
        parner, commodity, _ = create_basic()
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity, quantity=70)
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity, quantity=3)
        response = self.client.get(reverse('status'))
        object = response.json()
        self.assertEqual(object["count"], 1)
        self.assertEqual(object["results"][0]["quantity"], -73)

    def test_multiple_commodity(self):
        parner, commodity1, commodity2 = create_basic()
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity1, quantity=70)
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity1, quantity=3)
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity1, quantity=50)
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity1, quantity=4)
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity2, quantity=170)
        Inventory.objects.create(customer=parner, inventory_type='shipping', commodity=commodity2, quantity=13)
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity2, quantity=150)
        Inventory.objects.create(customer=parner, inventory_type='receiving', commodity=commodity2, quantity=14)
        response = self.client.get(reverse('status'))
        object = response.json()
        self.assertEqual(object["count"], 2)
        self.assertEqual(object["results"][0]["quantity"], -19)
        self.assertEqual(object["results"][1]["quantity"], -19)
