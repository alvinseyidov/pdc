from django.shortcuts import render
from portfolio.models import Category, Project
from haqqimizda.models import FAQ,Partnyorlar, Hashtag
from xidmetler.models import Xidmetler

# Create your views here.

def home(request):

    project_categories = Category.objects.all()
    projects = Project.objects.all()
    faq = FAQ.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    context = {
        "project_categories": project_categories,
        "projects": projects,
        "faq": faq,
        "xidmetler": xidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar
    }
    return render(request, "home.html", context)