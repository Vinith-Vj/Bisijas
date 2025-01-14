from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def about_us(request):
    return render(request, 'about_us.html')

def packages(request):
    return render(request, 'packages.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact_us(request):
    return render(request, 'contact_us.html')