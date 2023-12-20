from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    cdata = category.objects.all().order_by('-id')[0:6]
    data = notification.objects.all().order_by('-id')[0:4]

    return render(request, 'user/index.html', {"data": cdata, "notification": data})


def services(request):
    return render(request, 'user/services.html')


def about(request):
    return render(request, 'user/about.html')


def videogallery(request):
    vdata = video.objects.all().order_by('-id')
    return render(request, 'user/video.html', {'video': vdata})


def newsd(request):
    cdata = category.objects.all().order_by('-id')[0:6]
    ndata = news.objects.all().order_by('-id')[0:4]

    return render(request, 'user/viewsnews.html', {"data": cdata, "news": ndata})


def viewmore(request):
    a = request.GET.get('msg')
    ndata = news.objects.filter(id=a)
    return render(request, 'user/viewmore.html', {"data": ndata})


def Attacks(request):
    return render(request, 'user/Attacks.html')


def Devices(request):
    return render(request, 'user/Devices.html')


def Country(request):
    return render(request, 'user/Country.html')


def IT_News(request):
    return render(request, 'user/IT News.html')


def Contact(request):
    return render(request, 'user/Contactus.html')

