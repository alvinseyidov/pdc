from django.shortcuts import render
from .models import Project, Category
from xidmetler.models import Xidmetler
from haqqimizda.models import *
# Create your views here.

def portfolio(request):
    project_categories = Category.objects.all()
    projects = Project.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    context = {
        "project_categories": project_categories,
        "projects": projects,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "portfolio.html", context)


def portfoliodetail(request, id):
    project = Project.objects.get(pk=id)
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    context = {
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "project": project 
    }
    return render(request, "portfolio-detail.html", context)