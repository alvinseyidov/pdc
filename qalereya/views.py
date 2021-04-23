from django.shortcuts import render
from .models import Gallery

# Create your views here.

def qalereya(request):
    gallery = Gallery.objects.all()

    context = {
        "gallery": gallery
    }
    return render(request, "qalereya.html", context)