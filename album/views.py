from django.shortcuts import render, redirect
from .import forms
from .import models
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, ListView

from django.urls import reverse_lazy


# Create your views here.


class Add_Album(CreateView):
    template_name = "add_album.html"
    form_class = forms.AlbumForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)
    
class Show_Album( ListView):
    model= models.Album
    template_name='home.html'
    context_object_name = 'albums'
    # pk_url_kwarg = 'id'
    
    
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     album= self.object
    #     detail=album
    #     name= album.musician.first_name + album.musician.last_name
    #     email= album.musician.email
    #     instrument= album.musician.instrument
        
    #     context['title']=name
    #     context['email']=email
    #     context['instrument']=instrument
    #     context['detail']= detail
    #     return context
        