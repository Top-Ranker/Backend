from django.http.response import HttpResponse
from rest_framework import generics
# from django.shortcuts import render
# from rest_framework import permissions
# from rest_framework import serializers
# from rest_framework.serializers import Serializer
# from rest_framework.views import APIView
from .serializers import UserSerializer, ProblemSerializer, SubmissionSerializer
# from rest_framework.response import Response
# from .models import User, problems
# from rest_framework import status
# from django.contrib.auth.hashers import make_password
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import ProblemFilter,SubmissionFilter

from .models import *
from .serializers import UserSerializer



# Create your views here.
def index(request):
    return HttpResponse("Server Working!")


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        password = request.data['password']
        password = make_password(password=password)
        if serializer.is_valid():
            serializer.save(password=password)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    
    def get(self,request):
        userid = request.user
        user = User.objects.get(username=userid)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)

@api_view(['GET'])
def logout(request):
    from django.contrib.auth import logout
    request.user.auth_token.delete()
    logout(request)
    return Response({'message', 'Logged Out Successfully'})

#read-write endpoints to represent a collection of model instances.
class ProblemPostAPIView(generics.ListCreateAPIView): #detailview
    lookup_field = 'id'
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('Difficulty', 'Contributor', 'Visibility', 'domain', 'type')
    filter_class = ProblemFilter
    search_fields = ('Name')
    def get_queryset(self):
        return problems.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ProblemView(generics.RetrieveUpdateAPIView): #detailview
    lookup_field = 'id'
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    def get_queryset(self):
        return problems.objects.all()

#------------------------Submission views-------------------------------------
class SubmissionListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    filter_class = SubmissionFilter
    def get_queryset(self):
        return submissionA.objects.all()



