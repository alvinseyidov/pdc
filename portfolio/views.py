from django.shortcuts import render
from .models import Project, Category
from xidmetler.models import Xidmetler, KorporativXidmetler
from haqqimizda.models import *
# Create your views here.

def portfolio(request):
    project_categories = Category.objects.all()
    projects = Project.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "project_categories": project_categories,
        "projects": projects,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "new/projects.html", context)


def portfoliodetail(request, id):
    project = Project.objects.get(pk=id)
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "xidmetler": xidmetler,
        "kxidmetler": kxidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "project": project 
    }
    return render(request, "new/project.html", context)