from django.db import models

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='packages/')
    booking_link = models.URLField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Image"
    

class VideoCarousel(models.Model):
    # title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Poster(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title