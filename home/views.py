from django.shortcuts import render
from portfolio.models import Category, Project
from haqqimizda.models import FAQ
from xidmetler.models import Xidmetler

# Create your views here.

def home(request):

    project_categories = Category.objects.all()
    projects = Project.objects.all()
    faq = FAQ.objects.all()
    xidmetler = Xidmetler.objects.all()

    context = {
        "project_categories": project_categories,
        "projects": projects,
        "faq": faq,
        "xidmetler": xidmetler
    }
    return render(request, "home.html", context)