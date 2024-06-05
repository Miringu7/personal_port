from django.contrib import admin
from .models import Project, BlogPost, Testimonial

# Register your models here.
admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(Testimonial)