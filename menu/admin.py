from django.contrib import admin
from .models import Menu, MenuItem

# Register your models hereю

class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'created_at'
    ]

    class Meta:
        model = Menu


class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'parent',
        'url',
        'named_url'
    ]
    exclude = ['uni_url']

    class Meta:
        model = MenuItem

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
