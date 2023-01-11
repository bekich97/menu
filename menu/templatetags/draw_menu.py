from django import template
from django.urls import resolve

from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('tag_files/menu.html', takes_context=True)
def draw_menu(context, slug):
    if MenuItem.objects.filter(uni_url=context.request.path).first():
        current_item = MenuItem.objects.filter(uni_url=context.request.path).first()
    else:
        current_item = ""
    menu = Menu.objects.filter(slug=slug).first()
    menu_items = MenuItem.objects.filter(menu=menu, parent=None)
    if not menu:
        return {'menu': '', 'menu_items': menu_items, 'context': context, 'current_item': current_item}

    return {'menu': menu, 'menu_items': menu_items, 'context': context, 'current_item': current_item}
