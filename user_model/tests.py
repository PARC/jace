

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import *

class QuestionModelTests(TestCase):

    def test_modulo(self):
        """
        tests if given a date that is not every two weeks it returns false
        """
        time = timezone.now() + datetime.timedelta(days=30)
        non_twoweek= User(identifier="Joel",language="ENG",uuid="12345",timestamp=timezone.now(),deletedIndicator=False,
                          startdate=0,Days_since_start=17,Days_since_last_report=2)
        is_twoweek = User(identifier="Joel",language="ENG",uuid="12345",timestamp=timezone.now(),deletedIndicator=False,
                               startdate=0,Days_since_start=14,Days_since_last_report=2)
        self.assertIs(non_twoweek.time_to_change(), False)
        self.assertIs(is_twoweek.time_to_change(), True)
    def test_complete_build(self):


        u = User(identifier="Joel",language="ENG",uuid="12345",timestamp=timezone.now(),deletedIndicator=False,
                               startdate=0,Days_since_start=14,Days_since_last_report=2)


        i = Intervention(uuid="1234567",timestamp = timezone.now(),deletedIndicator = False,Name = "II",
                         Intervention_Type ="Implemntation",Setup_Complete=False,Is_On = False,startdate=1)


        """
        uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField()
    deletedIndicator = models.BooleanField()
    Name = models.CharField(max_length=UUID_FIELD)
    Reference_to_Intervention = models.ForeignKey(Intervention)
        """
        s = Survey(uuid="7711",timestamp=timezone.now(),deletedIndicator=False,Name="II1",Reference_to_Intervention=i)


        """
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
    preferenceToSet = models.CharField(max_length=MEDIUM_LENGTH)
    answers = models.CharField(max_length=MEDIUM_LENGTH)
    expireDate = models.IntegerField()
    expireTime = models.TimeField()
    Notify = models.BooleanField()
    Sequence = models.IntegerField()
    Name = models.CharField(max_length=UUID_FIELD)



        """
        q = Question(question_text = "Hello World",uuid="1771717",timestamp=timezone.now(),deletedIndicator = False,
                     responceType="Ask Now",tag = "Hello",choices ="[]",referenceToSurvey=s,reminders=False,askDate="2",
                     askTime='10:00',answers="",expireDate="99",expireTime="11:00",Notify=True,Sequence=1,Name="First")


        """ uuid = models.CharField(max_length=UUID_FIELD)
    timestamp = models.DateTimeField
    deletedIndicator = models.BooleanField
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
    Answered = models.BooleanField()"""
        a = Answer(uuid="9872",timestamp=timezone.now(),question=q,user=u,Answer_text="blah",Answered=True)

        self.assertIs(str(q),"Hello")
        self.assertIs(str(a), "blah")

