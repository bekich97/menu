from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def not_found(request):
    return render(request, 'not-found.html')
