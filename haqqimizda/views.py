from django.shortcuts import render
from .models import Gallery, FAQ
# Create your views here.

def haqqimizda(request):
    gallery = Gallery.objects.all()
    faq = FAQ.objects.all()

    context = {
        "gallery": gallery,
        "faq": faq
    }
    return render(request, "haqqimizda.html", context)


