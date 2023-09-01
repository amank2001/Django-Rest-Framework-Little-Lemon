from django.test import TestCase
from restaurant1.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title="Rossitto", Price=11, Inventory=15)
        Menu.objects.create(Title="Khaboos", Price=16, Inventory=10)
        Menu.objects.create(Title="Cakes", Price=9, Inventory=20)
        
    def test_getall(self):
         menu_objects = Menu.objects.all()
         
         serialized_menu = [
            {
                "Title": menu.Title,
                "Price": menu.Price,
                "Inventory": menu.Inventory,
            }
            for menu in menu_objects
        ]

         response_data = [
            {
                "Title": "Rossitto",
                "Price": 11,
                "Inventory": 15,
            },
            {
                "Title": "Khaboos",
                "Price": 16,
                "Inventory": 10,
            },
            {
                "Title": "Cakes",
                "Price": 9,
                "Inventory": 20,
            },
        ]

         self.assertEqual(serialized_menu, response_data)