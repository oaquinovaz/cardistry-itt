from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ObraArte

class User_Form(UserCreationForm):
    celular = forms.CharField(max_length=50)
    correo = forms.CharField(max_length=50)

