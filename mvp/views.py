from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def mainpage(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method=='POST':
        username1 = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username1, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request,'Yahooo everything is ok')
            return redirect('/')
        else:
            messages.error(request,'an error has occured')
            return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')