from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name= models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    email= models.EmailField()
    contact= models.CharField(max_length=11)
    instrument= models.CharField(max_length= 100)
    
    def __str__(self):
        return self.first_name
    
    