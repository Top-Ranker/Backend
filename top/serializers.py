from rest_framework import serializers

from .models import User, Problem, Submission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'country', 'age', 'field', 'profession', 'university')


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['question_id', 'name', 'type', 'description', 'difficulty', 'contributor', 'fitness_function',
                  'visibility', 'dimensions', 'domain', 'language']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'question_id', 'user_id', 'dimension', 'solution', 'time', 'score', 'input']
        read_only_fields = ['score', 'user_id', 'question_id']
