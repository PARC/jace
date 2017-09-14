# Create your models here.
from django.db import models
from django.contrib.postgres import fields
UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048


class User(models.Model):
    """
    The User's Model Representation

    """
    studyId = models.CharField(max_length=UUID_FIELD)
    language = models.CharField(max_length=UUID_FIELD)
    UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Days_since_start = models.IntegerField()
    Last_day_reported = models.IntegerField()
    Days_since_activty_start = models.IntegerField(blank=True)

    def __repr__(self):
        return str(self.identifier)

    def to_dictionary(self):
        return {"studyId": self.identifier, "language": self.language, "UUID": self.UUID,
                "Days_since_Start": self.Days_since_start, "Last_report": self.Days_since_last_report,
                "time_to_change": self.time_to_change()}


    def time_to_change(self):
        """
        Checks to see if the user is on a week break point to change JITAI
        :return: Boolian Value
        """
        try:
            if int(self.Days_since_start) % 14 == 0:
                return True
            else:
                return False
        except TypeError:
            return "Was Expecting an Integer"



class Survey(models.Model):
    """

    Survey Rep
    """
    UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)

    def __repr__(self):
        return self.Names

class Question(models.Model):
    question_text = models.CharField(max_length=SHORT_LENGTH)
    UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    responceType = models.CharField(max_length=MEDIUM_LENGTH)
    tag = models.CharField(max_length=MEDIUM_LENGTH)
    choices = fields.JSONField()
    referenceToSurvey = models.ForeignKey(to=Survey)
    reminders = models.BooleanField()
    askDate = models.IntegerField()
    askTime = models.TimeField()
    preferenceToSet = models.CharField(max_length=MEDIUM_LENGTH,blank=True)
    answers = fields.JSONField()
    expireDate = models.IntegerField()
    expireTime = models.TimeField()
    Notify = models.BooleanField(blank=True)
    Sequence = models.IntegerField()
    Name = models.CharField(max_length=UUID_FIELD)

    def __repr__(self):
        return self.tag





class Answer(models.Model):
    UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
    Answered = models.BooleanField()

    def __repr__(self):
        return self.Answer_text



