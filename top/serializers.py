from rest_framework import serializers
from .models import User, problems, submissionA


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','country','age','field','profession','university')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id', 'Name','type','Description','Difficulty', 'Contributor', 'Fitness_function','Visibility','dimensions', 'domain']
        read_only_fields = ['validity']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submissionA
        fields = ['question_id', 'user_id', 'dimensions', 'Solution', 'Score', 'time', 'submissionDesc']


