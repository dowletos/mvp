from django import forms
import re
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(label='Имя пользователя',help_text='max 150 symbols',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', help_text='max 150 symbols', widget=forms.TextInput(attrs={'class': 'form-control'}))