from django.shortcuts import render
from xidmetler.models import Xidmetler
from haqqimizda.models import *
# Create your views here.

def xidmetler(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    context = {
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "xidmetler.html",context)

def xidmetlerdetail(request, id):
    xidmet = Xidmetler.objects.get(pk=id)
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    context = {
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmet": xidmet
    }
    return render(request, "xidmetler-detail.html",context)