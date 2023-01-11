from .models import Menu
from django.urls import resolve


def menus(request):
    context = {
        # "menus": Menu.objects.filter(parent=None),
        # "url_name": resolve(request.path_info).url_name
    }
    return context