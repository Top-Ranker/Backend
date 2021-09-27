from django_filters import rest_framework as filters
from .models import problems, submissionA


class ProblemFilter(filters.FilterSet):
    class Meta:
        model = problems
        fields = ['Difficulty', 'Contributor', 'Visibility', 'domain', 'type']

class SubmissionFilter(filters.FilterSet):
    class Meta:
        model = submissionA
        fields = ['question_id', 'user_id']
