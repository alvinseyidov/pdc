from django.shortcuts import render
from .models import Project, Category
# Create your views here.

def portfolio(request):
    project_categories = Category.objects.all()
    projects = Project.objects.all()

    context = {
        "project_categories": project_categories,
        "projects": projects
    }
    return render(request, "portfolio.html", context)