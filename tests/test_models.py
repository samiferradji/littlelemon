from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):

    def setUp(self):
        pass


    def test_get_item(self):
        Menu.objects.create(Title="IceCream", Price=80.00, Inventory=100)
        item = Menu.objects.get(Title="IceCream")
        self.assertEqual(item.__str__(), "IceCream : 80.00")
