from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login

def mainpage(request):
    return render(request, 'index.html')


def user_login(request):
    f_name=request.POST['username']
    f_password = request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
    else:
        return HttpResponse("error login check please")
