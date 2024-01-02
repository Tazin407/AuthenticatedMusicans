from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    
    rate=[
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    name= models.CharField(max_length=30)
    release_date= models.DateField()
    rating= models.CharField(max_length= 2, choices= rate)
    musician= models.ForeignKey(Musician, on_delete= models.CASCADE, related_name='musician')
    
    def __str__(self):
        return self.name
    
    
    
   
