from django.shortcuts import render, redirect
from .models import Package, Gallery, VideoCarousel, Service, Poster
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

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
    posters = Poster.objects.all()
    return render(request, 'posters.html', {'posters': posters})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and phone and email and message:
            subject = f"New Contact Us Message from {name}"
            full_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(subject, full_message, email, [settings.EMAIL_HOST_USER],
                          fail_silently=False)
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                 messages.error(request, 'An error occurred while sending your message. Please try again later.')
        
        else:
            message.error(request, 'All Fields are required')

        return redirect('contactus')
    return render(request, 'contact_us.html')