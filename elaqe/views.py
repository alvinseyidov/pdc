from django.shortcuts import render
from xidmetler.models import Xidmetler
from haqqimizda.models import Partnyorlar
# Create your views here.

def elaqe(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    context = {
        "xidmetler": xidmetler,
        "partnyorlar": partnyorlar
    }
    return render(request, "elaqe.html",context)



   