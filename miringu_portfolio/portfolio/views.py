from django.shortcuts import render
from .models import Project, BlogPost, Testimonial

# Create your views here.
def index(request):
    projects = Project.objects.all()
    posts = BlogPost.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'projects': projects, 'posts': posts, 'testimonials': testimonials})