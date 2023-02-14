from django import forms
import re
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User,AbstractUser
from news.models import category,bankbase

class register_new_user_form(UserCreationForm):
    last_name = forms.CharField(max_length=250, label='Фамилия',required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=250, label='Имя',required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=250, label='Login', required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=250, label='Email', required=False, widget=forms.EmailInput(attrs={"class": "form-control"}))
    bankid_FK=forms.ModelChoiceField(label='Введите банковский идентификационный номер (БИН)', queryset=bankbase.objects.all() , widget=forms.Select(attrs={"class":"form-control"}))
    password1 =  forms.CharField(label='Пароль',required=False, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField( label='Повторите пароль',required=False, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    is_active=forms.BooleanField(label='Активирован ', widget=forms.CheckboxInput(attrs={"class":"form-control"}) )


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bankid_FK', 'password1', 'password2',)

