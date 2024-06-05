from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials')