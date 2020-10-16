from django.shortcuts import render
from .models import Project

# Create your views here.

def home (request):
    # create variable to get all project objects
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
