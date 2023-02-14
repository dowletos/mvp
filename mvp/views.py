from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from news.models import News,profiles,profilesIndex,View_UserSet
from .forms import register_new_user_form



def mainpage(request):

    UserSet=View_UserSet.objects.filter(username__exact=request.user)
    return render(request, 'login.html', { 'title': 'Добро пожаловать','UserSet':UserSet})


def users_edit(request):
    UserSet = View_UserSet.objects.filter(username__exact=request.user)

    if request.method == 'POST':
        NF = register_new_user_form(request.POST)
        print(NF.errors)
        if NF.is_valid():
            NF.save()
            return render(request, 'users_edit.html', {'NF': NF, 'title': 'Добро пожаловать', 'UserSet': UserSet})

    else:
        NF = register_new_user_form()
    return render(request, 'users_edit.html', {'NF': NF, 'title': 'Добро пожаловать', 'UserSet':UserSet})


def user_profile_settings(request):
    UserSet = View_UserSet.objects.filter(username__exact=request.user)

    if request.method == 'POST':
        NF = register_new_user_form(request.POST)
        if NF.is_valid():
            register_new_user_form.objects.create(NF.cleaned_data)
    else:
        NF = register_new_user_form()
    return render(request, 'profile.html', {'NF': NF, 'title': 'Добро пожаловать', 'UserSet': UserSet})


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



