from django.shortcuts import render

# Create your views here.


def yenilikler(request):
    return render(request, "yenilikler.html")