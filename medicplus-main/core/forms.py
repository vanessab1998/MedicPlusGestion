from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import usercontact, paciente, horaMedica
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    class Meta : 
        model = usercontact
        fields = '__all__'


class paceinteForm(forms.ModelForm):
    class Meta : 
        model = paciente
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta : 
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]

class horaMedicaForm(forms.ModelForm):
    class Meta : 
        model = horaMedica
        fields = '__all__'

