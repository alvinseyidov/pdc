from django.shortcuts import render
from xidmetler.models import Xidmetler
# Create your views here.

def xidmetler(request):
    xidmetler = Xidmetler.objects.all()
    context = {
        "xidmetler": xidmetler
    }
    return render(request, "xidmetler.html",context)