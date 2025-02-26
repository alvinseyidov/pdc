from django.shortcuts import render, get_object_or_404
from xidmetler.models import Xidmetler, KorporativXidmetler
from haqqimizda.models import *
from yenilikler.models import Yenilikler


# Create your views here.


def yenilikler(request):
    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    news = Yenilikler.objects.all()

    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler,
        "yenilikler": news  # Fetch all news
    }
    return render(request, "new/blogs.html", context)


def yeniliklerdetail(request, id):
    news_detail = get_object_or_404(Yenilikler, id=id)

    xidmetler = Xidmetler.objects.all()
    partnyorlar = Partnyorlar.objects.all()
    hashtaglar = Hashtag.objects.all()
    kxidmetler = KorporativXidmetler.objects.all()
    context = {
        "kxidmetler": kxidmetler,
        "partnyorlar": partnyorlar,
        "hashtaglar": hashtaglar,
        "xidmetler": xidmetler,
        "news_detail": news_detail
    }
    return render(request, "new/blog.html", context)
