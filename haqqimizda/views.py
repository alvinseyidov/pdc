from django.shortcuts import render
from .models import Gallery, FAQ
from xidmetler.models import Xidmetler
# Create your views here.

def haqqimizda(request):
    gallery = Gallery.objects.all()
    faq = FAQ.objects.all()
    xidmetler = Xidmetler.objects.all()

    context = {
        "gallery": gallery,
        "faq": faq,
        "xidmetler": xidmetler
    }
    return render(request, "haqqimizda.html", context)


