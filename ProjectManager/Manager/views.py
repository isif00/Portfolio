from django.shortcuts import render
from .models import Projects


def index(request):
    projects = Projects.objects.all()
    return render(request, 'main/index.html', {'projects': projects})


def handler404(request, exception):
    return render(request, '404.html', status=404)
