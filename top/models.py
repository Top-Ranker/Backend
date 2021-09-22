from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(null = True,blank=True)
    field = models.CharField(max_length=100,null=True,blank=True) 
    profession = models.CharField(max_length=100,null=True,blank=True) 
    university = models.CharField(max_length=100,null=True,blank=True)


class problems(models.Model):
    Difficulty_choices = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]
    Visibility_choices = [
        ('yes', 'yes'),
        ('no', 'no')
    ]
    type_choices = [
        ('Maximization', 'Maximization'),
        ('Minimization', 'Minimization')
    ]
    Name = models.CharField(max_length = 100)
    type = models.CharField(max_length=20, choices=type_choices)
    Description = models.TextField()
    Difficulty = models.CharField(max_length = 20, choices=Difficulty_choices)
    Fitness_function = models.TextField()
    Contributor = models.ForeignKey(User, on_delete = models.CASCADE)
    Visibility = models.CharField(max_length= 20, choices = Visibility_choices)
    dimensions = models.IntegerField()
    domain = models.CharField(max_length = 100)
    validity = models.BooleanField(default=0, null=True, blank=True)

    def __str__(self):
        return self.Name


# class submissionB(models.Model):
#     solution = models.TextField()
#     score = models.IntegerField()
#     dimensions_of_sol = models.IntegerField()
#     solver = models.ForeignKey(User, on_delete = models.CASCADE)
#
#
# class submissionA(models.Model):
#     question_id = models.ForeignKey(problems, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     dimensions = models.IntegerField()
#     Solution = models.TextField()
#     Score = models.IntegerField()
#     time = models.TimeField()
#
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
