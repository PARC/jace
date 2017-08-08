from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

UUID_FIELD = 3

class Intervention(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator =models.BooleanField()
    Name = models.CharField(max_length=36)
    Intervention_Type = models.CharField(max_length=36)
    Setup_Complete = models.BooleanField()
    Is_On = models.BooleanField()
    startdate = models.IntegerField()



class Survey(models.Model):
    uuid_length = 36
    uuid = models.CharField(max_length=uuid_length)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=36)
    Reference_to_Intervention = models.ForeignKey(Intervention)



class Question(models.Model):
    uuid_length = 36
    question_text = models.CharField(max_length=200)
    uuid = models.CharField(max_length=uuid_length)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    responceType = models.CharField(max_length=1024)
    responceTypeTime = models.DateTimeField(blank=True)
    tag = models.CharField(max_length=1024)
    choices = models.CharField(max_length=1024)
    referenceToSurvey = models.ForeignKey(to=Survey)
    reminders = models.BooleanField()
    askDate = models.IntegerField()
    askTime = models.TimeField()
    preferenceToSet = models.CharField(max_length=1024)
    answers = models.CharField(max_length=1024)
    expireDate = models.IntegerField()
    expireTime = models.TimeField()
    Notify = models.BooleanField()
    Sequence = models.IntegerField()
    Name = models.CharField(max_length=36)

    def __str__(self):
        return self.question_text,

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class User(models.Model):
    identifier = models.CharField(max_length=36)
    language = models.CharField(max_length=3)
    uuid = models.CharField(max_length=36)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    startdate = models.IntegerField()
    Days_since_start = models.IntegerField()
    Days_since_last_report = models.IntegerField()

class Answer(models.Model):
    uuid = models.CharField(max_length=36)
    timestamp = models.DateTimeField
    deletedIndicator = models.BooleanField
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Answer_text = models.CharField(max_length=1024)
    Answered = models.BooleanField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
