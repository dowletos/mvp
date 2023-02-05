from django.shortcuts import render
from django.http import HttpResponse

from .models import News,profiles,profilesIndex


def index(request):
    news=News.objects.order_by('-created_at')

    return render(request,'news/index.html',{'news':news,'title':'My title from DB'})
