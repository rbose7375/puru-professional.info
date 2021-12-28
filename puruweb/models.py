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


class signp(models.Model):
    name=models.CharField(max_length=50)  
    userName=models.CharField(max_length=50)
    email =models.EmailField(max_length=254)  
    passwd=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.userName

  
class personal(models.Model):
    name=models.CharField(max_length=500)
    age=models.DateTimeField(auto_now=False, auto_now_add=False)
    relation=models.CharField( max_length=500)
    phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    occupation=models.CharField(max_length=500)
    mothertounge=models.CharField(max_length=500)
    img=models.ImageField(upload_to='image/personal')


    def __str__(self):
        return self.name

<<<<<<< HEAD
class gallary(models.Model):
    file=models.FileField(upload_to='gallary/')
    name=models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.name

=======
>>>>>>> 02329d5 (tatti gallary)

