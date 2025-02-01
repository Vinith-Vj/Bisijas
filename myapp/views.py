from django.shortcuts import render
from .models import Package, Gallery, VideoCarousel, Service

# Create your views here.


def index(request):
    videos = VideoCarousel.objects.all()
    services = Service.objects.all()
    return render(request, 'index.html', {
        'videos': videos,
        'services': services,
    })

def base(request):
    return render(request, 'base.html')

def about_us(request):
    return render(request, 'about_us.html')

def packages(request):
    all_packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': all_packages})

# def gallery(request):
#     images = Gallery.objects.all()
#     return render(request, 'gallery.html', {'images': images})

def gallery(request):
    images = list(Gallery.objects.all())  # Fetch all images

    # Group into alternating patterns
    patterns = []
    for i in range(0, len(images), 6):
        group = images[i:i+6]
        patterns.append({
            "column1": group[:3],  # First column: 1 large, 2 small
            "column2": group[3:]   # Second column: 2 small, 1 large
        })

    return render(request, "gallery.html", {"patterns": patterns})

def poster(request):
    return render(request, 'posters.html')

def contact_us(request):
    return render(request, 'contact_us.html')