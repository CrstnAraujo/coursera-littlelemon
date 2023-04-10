from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Icecream', price=80, inventory=100)
        self.assertEqual(item, 'Icecream: 80')