from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(null = True,blank=True)
    field = models.CharField(max_length=100,null=True,blank=True) 
    profession = models.CharField(max_length=100,null=True,blank=True) 
    university = models.CharField(max_length=100,null=True,blank=True) 