from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Icecream', price=80.20, inventory=100)
        self.assertEqual(item.title, 'Icecream')
        self.assertEqual(item.price, 80.20)
        self.assertEqual(item.inventory, 100)