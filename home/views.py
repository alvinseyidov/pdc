from yenilikler.models import Yenilikler
from django.shortcuts import render
from portfolio.models import Category, Project
from haqqimizda.models import FAQ,Partnyorlar, Hashtag
from xidmetler.models import Xidmetler, KorporativXidmetler
from yenilikler.models import *

# Create your views here.

def home(request):

    project_categories = Category.objects.all()
    projects = Project.objects.all()[:5]
    faq = FAQ.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    yenilikler = Yenilikler.objects.all()[:3]

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "project_categories": project_categories,
        "projects": projects,
        "faq": faq,
        "xidmetler": xidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "yenilikler": yenilikler
    }
    return render(request, "new/index.html", context)