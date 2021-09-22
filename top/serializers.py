from rest_framework import serializers
from .models import User, problems


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','country','age','field','profession','university')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id', 'Name','type','Description','Difficulty','Contributor', 'Fitness_function','Visibility','dimensions', 'domain']
        read_only_fields = ['validity']

    # converts to json
    # validation for data passed

