from django.shortcuts import render, redirect
from django.contrib import messages

from haqqimizda.models import Partnyorlar, Hashtag
from xidmetler.models import Xidmetler
from .forms import ContactForm

def elaqe(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi!")
            return redirect('elaqe')  # Redirect to clear form fields and avoid resubmission issues

    context = {
        "xidmetler": xidmetler,
        "hashtaglar": hashtaglar,
        "partnyorlar": partnyorlar,
        "form": form
    }
    return render(request, "elaqe.html", context)
