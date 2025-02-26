from django.shortcuts import render
from xidmetler.models import Xidmetler, KorporativXidmetler
from haqqimizda.models import *
# Create your views here.

def xidmetler(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "new/services.html",context)

def kxidmetler(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "new/corservices.html",context)

def xidmetlerdetail(request, id):
    xidmet = Xidmetler.objects.get(pk=id)
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    xidmetler = Xidmetler.objects.all()
    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "xidmetler": xidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmet": xidmet
    }
    return render(request, "new/service.html",context)