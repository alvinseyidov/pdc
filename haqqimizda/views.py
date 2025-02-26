from django.shortcuts import render
from .models import Gallery, FAQ
from xidmetler.models import Xidmetler, KorporativXidmetler
from haqqimizda.models import *
# Create your views here.

def haqqimizda(request):
    gallery = Gallery.objects.all()
    faq = FAQ.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "gallery": gallery,
        "faq": faq,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "new/about.html", context)


