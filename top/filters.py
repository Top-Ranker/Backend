from django_filters import rest_framework as filters
from .models import Problems, Submission


class ProblemFilter(filters.FilterSet):
    class Meta:
        model = Problems
        fields = ['Difficulty', 'Contributor', 'Visibility', 'domain', 'type']

class SubmissionFilter(filters.FilterSet):
    class Meta:
        model = Submission
        fields = ['question_id', 'user_id']
