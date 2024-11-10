from django.db import models

# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=100)
    movie=models.CharField(max_length=100)
    date=models.DateField()
    
class Geust(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    
class Resevation(models.Model):
    guest=models.ForeignKey(Geust,on_delete=models.CASCADE,related_name='reservation')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reservation')
    