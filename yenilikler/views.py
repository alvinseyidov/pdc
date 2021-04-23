from django.shortcuts import render
from xidmetler.models import Xidmetler
# Create your views here.


def yenilikler(request):
    xidmetler = Xidmetler.objects.all()
    context = {
        "xidmetler": xidmetler
    }
    return render(request, "yenilikler.html",context)