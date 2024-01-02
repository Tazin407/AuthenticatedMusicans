from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

# Create your views here.

class Add_Musician(CreateView):
    template_name='add_musician.html'
    form_class= forms.MusicianForm
    success_url= reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form= forms.SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created successfully')
                form.save()
                return redirect('user_login')
        
        form= forms.SignupForm()
        return render(request, 'login.html', {'form': form})    
    
    else:
        return redirect('home')        
    
    
def user_login(request):
    if request.method=='POST':
        form= AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name= form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            
            user= authenticate(username= name, password= user_pass)
            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.error('Wrong Info. try again')
                return redirect('user_login')
        
    form= AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

