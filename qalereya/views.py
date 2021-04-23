from django.shortcuts import render
from .models import Gallery
from xidmetler.models import Xidmetler
# Create your views here.

def qalereya(request):
    gallery = Gallery.objects.all()
    xidmetler = Xidmetler.objects.all()

    context = {
        "gallery": gallery,
        "xidmetler": xidmetler
    }
    return render(request, "qalereya.html", context)