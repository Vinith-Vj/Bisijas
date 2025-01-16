from django.contrib import admin
from .models import Package, Gallery, VideoCarousel, Service

# Register your models here.

admin.site.register(Package)
# class PackageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description')

admin.site.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('image', 'caption')

admin.site.register(VideoCarousel)

admin.site.register(Service)