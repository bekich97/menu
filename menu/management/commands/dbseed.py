from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem
from random import randint

class Command(BaseCommand):
    help = 'Database seed command for insert some data if menu table is empty'

    def add_arguments(self, parser):
        parser.add_argument('menu_count', type=int, help='Indicates the number of menus to be created')
        parser.add_argument('menuitem_count', type=int, help='Indicates the number of menu items to be created')

    def handle(self, *args, **kwargs):
        menu_count = kwargs['menu_count']
        menuitem_count = kwargs['menuitem_count']

        # Seed for menu
        menus = Menu.objects.all()
        if not menus:
            for i in range(menu_count):
                menu = Menu()
                menu.title = "Menu-" + str(i+1)
                menu.slug = "menu-" + str(i+1)
                menu.save()

        # Seed for menu item table
        menu_items = MenuItem.objects.all()
        if not menu_items:
            for i in range(menuitem_count-1):
                menu = MenuItem()
                menu.menu = Menu.objects.order_by('?')[0]
                menu.title = "MenuItem-" + str(i+1)
                menu.parent = MenuItem.objects.order_by('?')[0] if i != 0 and randint(0, 1) else None
                menu.url = "/menu-" + str(i+1)
                menu.save()
            
            menu = MenuItem()
            menu.menu = Menu.objects.order_by('?')[0]
            menu.title = "Test for named URL"
            menu.parent = MenuItem.objects.order_by('?')[0] if randint(0, 1) else None
            menu.url = "/test-1"
            menu.named_url = "test-named"
            menu.save()

        print("DB seed completed successfully!")