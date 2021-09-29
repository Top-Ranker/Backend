from django.http.response import HttpResponse
from .serializers import UserSerializer, ProblemSerializer, SubmissionSerializer
from .models import User, Problem,Submission,BearerAuthentication,Dimension
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import requests
import json

auth_key = '8Tj4MPqAI7;_oZU`C5Ni' # Randomly Generated String in Python


# Create your views here.
def index(request):
    return HttpResponse("Server Working!")


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if "password" not in list(request.data.keys()):
            return Response({
                "message" : "Password Field Missing!"
                })
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
    request.user.auth_token.delete()
    logout(request)
    return Response({'message', 'Logged Out Successfully'})

class ProblemView(viewsets.ViewSet):
    def list(self,request):
        if 'filter' not in list(request.data.keys()):
            return Response({
                "message" : "filter Field Missing" })
        filter = request.data['filter']
        if filter not in ["Easy","Medium","Hard","Any"]:
            return Response({
                "message" : "Filter must be in Easy, Medium, Hard or Any"
            })
        
        if filter == 'Any':
            problems = Problem.objects.all()
        else: 
            problems = Problem.objects.filter(difficulty= filter)
        serializer = ProblemSerializer(problems,many=True)
        return Response(serializer.data)


    
    def retrieve(self,request,pk):
        problems = Problem.objects.all()

        problem = get_object_or_404(problems, question_id=pk)
        serializer= ProblemSerializer(problem)
        return Response(serializer.data)


class ProblemAddView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    serializer_class = ProblemSerializer

    def post(self,request):
        userid = request.user
        serializer = ProblemSerializer(data = request.data)
        data = request.data['dimensions']
        for elem in data : 
            if not Dimension.objects.filter(dimension = elem).exists():
                Dimension.objects.create(dimension = elem)
        if serializer.is_valid():
            serializer.save(contributor = userid)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddSubmission(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]
    serializer_class = Submission

    def post(self,request):
        userid = request.user
        serializer = SubmissionSerializer(data = request.data)
        question_id = request.data['question_id']
        dimension = int(request.data['dimension'])
      

        available_dimensions = list(Problem.objects.filter(question_id = question_id).values_list('dimensions',flat=True))
        if dimension not in available_dimensions:
            return Response({
                "message" : "Dimension provided not available for this problem"
            })

        if serializer.is_valid():
            question = Problem.objects.get(question_id=question_id)
            data = {}
            data['language'] = question.language # To be changed later
            data['code'] = question.fitness_function
            data['input'] = request.data['input']
            data['authkey'] = auth_key
            url = "http://localhost:8000/api/code"
            payload = json.dumps(data)
            headers = {
            'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            response_data = json.loads(response.text)
            score_recieved = int(response_data['output'])
            if question.type == "Minimization":
                score_recieved = -score_recieved
            serializer.save(question_id = Problem.objects.get(question_id=question_id),user_id = userid,score = score_recieved)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class SubmissionView(viewsets.ViewSet):
    serializer_class = Submission
    
    def list(self,request):
        keys = list(request.data.keys())
        if 'type' not in keys:
            return Response({
                "message" : "Type Required"
            })
        type = request.data['type']
        if type == "user":
            if 'userid' not in keys:
                return Response({
                    "message" : "Userid Required !"
                })
            userid = request.data['userid']
            if not User.objects.filter(username = userid).exists():
                return Response({
                    "message" : "User Id Not found in database"
                })
            submissions = Submission.objects.filter(user_id = userid)
            serializer = SubmissionSerializer(submissions,many=True)
            return Response(serializer.data)

        elif type == "problem":
            if 'questionid' not in keys:
                return Response({
                    "message" : "questionid Required"
                })
            questionid = request.data['questionid']
            if not Problem.objects.filter(question_id = questionid).exists():
                return Response({
                    "message" : "Question ID Not found in database!"
                })
            submissions = Submission.objects.filter(question_id = questionid)
            serializer = SubmissionSerializer(submissions,many=True)
            return Response(serializer.data)

        return Response({
            "message" : "Invalid Type Selected ! Valid ones are user and problem"
        })

    def retrieve(self,request,pk):
        submissions = Submission.objects.all()
        submission = get_object_or_404(submissions, question_id=pk)
        serializer= ProblemSerializer(submission)
        return Response(serializer.data)
        




        



# class ProblemPostAPIView(generics.ListCreateAPIView): 
#     lookup_field = 'id'
#     serializer_class = ProblemSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [BearerAuthentication]
#     filter_backends = (filters.DjangoFilterBackend, SearchFilter)
#     # filterset_fields = ('Difficulty', 'Contributor', 'Visibility', 'domain', 'type')
#     filter_class = ProblemFilter
#     search_fields = ('Name')
#     def get_queryset(self):
#         return Problems.objects.all()

#     def perform_create(self, serializer):
#         serializer.save()


# class ProblemView(generics.RetrieveUpdateAPIView): 
#     lookup_field = 'id'
#     serializer_class = ProblemSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [BearerAuthentication]
#     def get_queryset(self):
#         return problems.objects.all()

# class SubmissionListView(generics.ListAPIView):
#     lookup_field = 'id'
#     serializer_class = SubmissionSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [BearerAuthentication]
#     filter_class = SubmissionFilter
#     def get_queryset(self):
#         return Submission.objects.all()



