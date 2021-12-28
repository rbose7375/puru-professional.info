from django.db import models
from datetime import datetime, date

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=150)
    email=models.EmailField( max_length=254)
    phone=models.IntegerField()
    reason=models.CharField( max_length=150)
    explain=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name=models.CharField( max_length=150)
    email=models.EmailField( max_length=254)
    phone=models.IntegerField()
    reason=models.CharField( max_length=150)
    explain=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class signp(models.Model):
    name=models.CharField(max_length=50)  
    userName=models.CharField(max_length=50)
    email =models.EmailField(max_length=254)  
    passwd=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.userName

  
