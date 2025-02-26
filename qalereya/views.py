from django.shortcuts import render
from .models import Gallery
from xidmetler.models import Xidmetler, KorporativXidmetler
from haqqimizda.models import *
# Create your views here.

def qalereya(request):
    gallery = Gallery.objects.all()
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "gallery": gallery,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler
    }
    return render(request, "new/gallery.html", context)