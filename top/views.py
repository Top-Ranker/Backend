from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import UserSerializer


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

    def get(self, request):
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
