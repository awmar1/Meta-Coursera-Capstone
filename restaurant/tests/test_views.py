from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        """Create test instances of the Menu model."""
        self.menu1 = Menu.objects.create(title="Pasta", price=12.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Pizza", price=15.99, inventory=5)
        self.menu3 = Menu.objects.create(title="Salad", price=9.99, inventory=8)
        self.client = APIClient()

    def test_get_all_menu_items(self):
        """Retrieve all Menu objects and compare with serialized data."""
        response = self.client.get(reverse('menu-list'))  # Assuming the URL name is 'menu-list'

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
