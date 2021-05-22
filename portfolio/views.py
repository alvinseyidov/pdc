from django.shortcuts import render
from .models import Project, Category
from xidmetler.models import Xidmetler
# Create your views here.

def portfolio(request):
    project_categories = Category.objects.all()
    projects = Project.objects.all()
    xidmetler = Xidmetler.objects.all()

    context = {
        "project_categories": project_categories,
        "projects": projects,
        "xidmetler": xidmetler
    }
    return render(request, "portfolio.html", context)


def portfoliodetail(request, id):
    project = Project.objects.filter(id=id)
    xidmetler = Xidmetler.objects.all()

    context = {
        "project": project
    }
    return render(request, "portfolio-detail.html", context)