from django.shortcuts import render
from xidmetler.models import Xidmetler
from haqqimizda.models import Partnyorlar, Hashtag
# Create your views here.

def elaqe(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    context = {
        "xidmetler": xidmetler,
        "hashtaglar": hashtaglar,
        "partnyorlar": partnyorlar
    }
    return render(request, "elaqe.html",context)



   