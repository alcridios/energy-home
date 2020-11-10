from django.db import models

# Create your models here.

class datos(models.Model):
    nombre=models.CharField(max_length=30)
    comuna=models.CharField(max_length=30)
    email=models.EmailField()
    fono=models.CharField(max_length=12)
    mensaje=models.CharField(max_length=500)