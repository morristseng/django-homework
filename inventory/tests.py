from django.test import TestCase
from django.urls import reverse
from model_bakery import baker


class ListInventoryStatusTests(TestCase):
    def setUp(self):
        self.commodity1 = baker.make('inventory.Commodity')
        self.commodity2 = baker.make('inventory.Commodity')

    def test_receiving_quantity(self):
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='receiving',
            commodity=self.commodity1,
            quantity=50)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='receiving',
            commodity=self.commodity1,
            quantity=4)
        response = self.client.get(reverse('status'))
        response_json = response.json()
        self.assertEqual(response_json["count"], 1)
        self.assertEqual(response_json["results"][0]["quantity"], 54)

    def test_shipping_quantity(self):
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='shipping',
            commodity=self.commodity1,
            quantity=70)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='shipping',
            commodity=self.commodity1,
            quantity=3)
        response = self.client.get(reverse('status'))
        response_json = response.json()
        self.assertEqual(response_json["count"], 1)
        self.assertEqual(response_json["results"][0]["quantity"], -73)

    def test_multiple_commodity(self):
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='shipping',
            commodity=self.commodity1,
            quantity=70)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='shipping',
            commodity=self.commodity1,
            quantity=3)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='receiving',
            commodity=self.commodity1,
            quantity=50)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity1.customer,
            inventory_type='receiving',
            commodity=self.commodity1,
            quantity=4)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity2.customer,
            inventory_type='shipping',
            commodity=self.commodity2,
            quantity=170)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity2.customer,
            inventory_type='shipping',
            commodity=self.commodity2,
            quantity=13)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity2.customer,
            inventory_type='receiving',
            commodity=self.commodity2,
            quantity=150)
        baker.make(
            'inventory.Inventory',
            customer=self.commodity2.customer,
            inventory_type='receiving',
            commodity=self.commodity2,
            quantity=14)
        response = self.client.get(reverse('status'))
        response_json = response.json()
        self.assertEqual(response_json["count"], 2)
        self.assertEqual(response_json["results"][0]["quantity"], -19)
        self.assertEqual(response_json["results"][1]["quantity"], -19)
