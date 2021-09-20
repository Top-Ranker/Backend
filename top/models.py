from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication import TokenAuthentication


class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(null = True,blank=True)
    field = models.CharField(max_length=100,null=True,blank=True) 
    profession = models.CharField(max_length=100,null=True,blank=True) 
    university = models.CharField(max_length=100,null=True,blank=True)


class BearerAuthentication(TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'

