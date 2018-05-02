from django.db import models
from django.contrib.auth.models import User

import datetime
import uuid

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    due_date = models.DateField()

    def status(self):
        # determine is session is past due
        
        if self.due_date > datetime.date.today:
            return 'New Training'
        else:
            return 'Past Due'

    def __str__(self):
        return self.title

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question

class Choices(models.Model):
    choices_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    seq = models.IntegerField()
    choice = models.CharField(max_length=1000)
    anwser = models.BooleanField()



class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, default='OPEN') # status are OPEN and COMPLETED

class Results(models.Model):
    results_id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5,decimal_places=2)
    completed_date = models.DateTimeField(default=datetime.datetime.now)

class ResultDetails(models.Model):
    results_details_id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
