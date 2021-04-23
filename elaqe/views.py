from django.shortcuts import render
from xidmetler.models import Xidmetler
# Create your views here.

def elaqe(request):
    xidmetler = Xidmetler.objects.all()
    context = {
        "xidmetler": xidmetler
    }
    return render(request, "elaqe.html",context)