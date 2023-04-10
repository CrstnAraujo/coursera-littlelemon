from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    test_data = {
        "title": "IceCream",
    }

    def setUp(self) -> None:
        self.ice_cream = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.hot_dog = Menu.objects.create(title="Hot Dog", price=20, inventory=50)
        self.pizza = Menu.objects.create(title="Pizza", price=60, inventory=25)

    def test_getall(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')

        serializer = MenuSerializer(Menu.objects.all(), many=True)
        serialized_data = JSONRenderer().render(serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serialized_data, response.content)