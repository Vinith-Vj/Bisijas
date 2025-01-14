from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('aboutus', views.about_us, name='aboutus'),
    path('packages', views.packages, name='packages'),
    path('gallery', views.gallery, name='gallery'),
    path('contactus', views.contact_us, name='contactus'),
]
