from rest_framework import serializers

from .models import User, Problem, Submission, Dimension


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'country', 'age', 'field', 'profession', 'university')


class DimensionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = ['dimension']


class ProblemSerializer(serializers.ModelSerializer):
    dimensions = DimensionsSerializer(many=True)

    class Meta:
        model = Problem
        fields = ['id', 'name', 'type', 'description', 'difficulty', 'contributor', 'fitness_function', 'dimensions',
                  'domain', 'language']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'question_id', 'user_id', 'dimension', 'solution', 'time', 'score', 'input']
        read_only_fields = ['score', 'user_id', 'question_id']

# "id": 1,
# "name": "Problem Name 0",
# "difficulty": "Easy",
# "domain": "Multi Model",
# "fitness_function": "inp = int(input())\r\nprint(inp)",
# "language": "Python",
# "dimension": [
#     {
#         "dimension": 25,
#         "participationD": 0
#     },
#     {
#         "dimension": 50,
#         "participationD": 0
#     },
#     {
#         "dimension": 100,
#         "participationD": 0
#     }
# ],
# "participationAll": 0
