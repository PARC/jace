# Create your models here.
"""
Main API Code
Joel Schooler
"""
from django.db import models

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048


class User(models.Model):
    """
    The User's Model Representation

    """
    identifier = models.CharField(max_length=UUID_FIELD)
    language = models.CharField(max_length=UUID_FIELD)
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    startdate = models.IntegerField()
    Days_since_start = models.IntegerField()
    Days_since_last_report = models.IntegerField()

    def __repr__(self):
        return str(self.identifier)

    def to_dictionary(self):
        return {"identifier": self.identifier, "language": self.language, "UUID": self.uuid,
                'startdate': self.startdate,
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

    class Meta:
        ordering = ('timestamp',)


class Intervention(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)
    Intervention_Type = models.CharField(max_length=UUID_FIELD)
    Setup_Complete = models.BooleanField()
    Is_On = models.BooleanField()
    startdate = models.IntegerField()
    reference_to_user = models.ForeignKey(User)

    def __repr__(self):
        return self.Name

    def to_dict(self):
        return {"uuid": self.uuid, "name": self.Name, "InterventionType": self.Intervention_Type, "Is_On": self.Is_On}


class Survey(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)
    Reference_to_Intervention = models.ForeignKey(Intervention)

    def __repr__(self):
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
    preferenceToSet = models.CharField(max_length=MEDIUM_LENGTH, blank=True)
    answers = models.CharField(max_length=MEDIUM_LENGTH)
    expireDate = models.IntegerField()
    expireTime = models.TimeField()
    Notify = models.BooleanField()
    Sequence = models.IntegerField()
    Name = models.CharField(max_length=UUID_FIELD)

    def __repr__(self):
        return self.tag


class Answer(models.Model):
    uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
    Answered = models.BooleanField()

    def __repr__(self):
        return self.Answer_text
