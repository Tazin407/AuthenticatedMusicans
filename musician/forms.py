from django import forms
from .import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model=models.Musician
        fields= '__all__'
        labels=[
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
            ('email', 'Email'),
            ('contact', 'Contact No'),
            ('instrument', 'Instrument'),
        ]
        
class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email']
        labels=[
            ('username', 'Username'),
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
            ('email', 'Email'),
        ]
        
