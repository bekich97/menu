from django.shortcuts import render, redirect
from .models import MenuItem

# Create your views here.

def url_view(request, url):
    full_url = "/" + url
    menu = MenuItem.objects.filter(url=full_url).first()
    if not menu:
        return redirect('/not-found')
    context = {
        "url_menu": menu
    }
    return render(request, 'url.html', context)


def test(request):
    return render(request, 'test.html')
