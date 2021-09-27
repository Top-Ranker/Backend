from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication import TokenAuthentication


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True,default="temp")
    email = models.EmailField(unique=True,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(null = True,blank=True)
    field = models.CharField(max_length=100,null=True,blank=True)
    profession = models.CharField(max_length=100,null=True,blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


class BearerAuthentication(TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.
    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:
    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'

class Dimension(models.Model):
    dimension = models.SmallIntegerField(primary_key=True)

    def __str__(self):
        return str(self.dimension)

class Problem(models.Model):
    difficulty_choices = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]

    type_choices = [
        ('Maximization', 'Maximization'),
        ('Minimization', 'Minimization')
    ]
    question_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length=20, choices=type_choices)
    description = models.TextField()
    difficulty = models.CharField(max_length = 20, choices=difficulty_choices)
    fitness_function = models.TextField(null = True)
    contributor = models.ForeignKey(User, on_delete = models.CASCADE, null=True,to_field='username')
    visibility = models.BooleanField(default=True,null=False)
    dimensions = models.ManyToManyField(Dimension)
    domain = models.CharField(max_length = 100)

class Submission(models.Model):
    question_id = models.ForeignKey(Problem, on_delete=models.CASCADE,to_field='question_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username')
    dimension = models.ForeignKey(Dimension,on_delete=models.CASCADE,to_field='dimension')
    solution = models.TextField()
    score = models.IntegerField()
    time = models.TimeField(auto_now=True)
    submissionDesc = models.TextField()

#
# class Contest(models.Model):
#     type_choices = (
#         ("conference", "conference"),
#         ("classtest", "classtest")
#     )
#     type = models.CharField(choices=type_choices, max_length=100)
#     hostedby = models.ForeignKey(User, on_delete=models.CASCADE)
#     prizepool = models.TextField(max_length=500)
#     problems = models.ManyToManyField(problems, related_name="problems", blank=True)
#     enrolled = models.ManyToManyField(User, related_name="Enrolled", blank=True)
#
# class ContestSubmissionHistory(models.Model):
#     contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="Submissions_for_which_contest")
#     submissions = models.ForeignKey(submissionA, on_delete=models.CASCADE, related_name="submissions_for_question")
