from django import forms
from .import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model= models.Album
        fields= '__all__'
        labels={
            'name': 'Title',
            'release_date': 'Released',
            'rating': 'Rating',
            'musician': 'Album by',
        }
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
