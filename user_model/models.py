from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048

class User(models.Model):
    identifier = models.CharField(max_length=UUID_FIELD)
    language = models.CharField(max_length=UUID_FIELD)
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    startdate = models.IntegerField()
    Days_since_start = models.IntegerField()
    Days_since_last_report = models.IntegerField()

    def __str__(self):
        return ("{}".format(self.identifier))


    def time_to_change(self):
        try:
            if int(self.Days_since_start) % 14 == 0:
                return True
            else:
                return False
        except TypeError:
            return "Was Expecting an Integer"


class Intervention(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)
    Intervention_Type = models.CharField(max_length=UUID_FIELD)
    Setup_Complete = models.BooleanField()
    Is_On = models.BooleanField()
    startdate = models.IntegerField()

    def __str__(self):
        return self.Name


class Survey(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)
    Reference_to_Intervention = models.ForeignKey(Intervention)

    def __str__(self):
        return self.Names


class Question(models.Model):
    question_text = models.CharField(max_length=SHORT_LENGTH)
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    responceType = models.CharField(max_length=MEDIUM_LENGTH)
    responceTypeTime = models.DateTimeField(blank=True)
    tag = models.CharField(max_length=MEDIUM_LENGTH)
    choices = models.CharField(max_length=MEDIUM_LENGTH)
    referenceToSurvey = models.ForeignKey(to=Survey)
    reminders = models.BooleanField()
    askDate = models.IntegerField()
    askTime = models.TimeField()
    preferenceToSet = models.CharField(max_length=MEDIUM_LENGTH,blank=True)
    answers = models.CharField(max_length=MEDIUM_LENGTH)
    expireDate = models.IntegerField()
    expireTime = models.TimeField()
    Notify = models.BooleanField()
    Sequence = models.IntegerField()
    Name = models.CharField(max_length=UUID_FIELD)

    def __str__(self):
        return self.tag





class Answer(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
    Answered = models.BooleanField()

    def __str__(self):
        return self.Answer_text



