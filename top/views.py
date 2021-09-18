from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.
def index(request):
    return HttpResponse("Server Working!")


class RegisterView(APIView):  
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        password = request.data['password']
        password = make_password(password=password)
        if serializer.is_valid():
            serializer.save(password=password)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get(self,request):
        userid = request.user
        user = User.objects.get(username=userid)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)

    