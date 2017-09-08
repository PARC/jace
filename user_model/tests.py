

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone
from communications.models import *
from .models import *

class QuestionModelTests(TestCase):
    u = User(identifier="Joel", language="ENG", UUID="12345", timestamp=timezone.now(), deletedIndicator=False,
             Days_since_start=14, Days_since_last_report=2)

    """
    uuid = models.CharField(max_length=UUID_FIELD)
timestamp = models.DateTimeField()
deletedIndicator = models.BooleanField()
Name = models.CharField(max_length=UUID_FIELD)
Reference_to_Intervention = models.ForeignKey(Intervention)
    """
    s = Survey(UUID="7711", timestamp=timezone.now(), deletedIndicator=False, Name="II1")

    """
    question_text = models.CharField(max_length=SHOzRT_LENGTH)
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
    q = Question(question_text="Hello World", UUID="1771717", timestamp=timezone.now(), deletedIndicator=False,
                 responceType="Ask Now", tag="Hello", choices={}, referenceToSurvey=s, reminders=False, askDate="2",
                 askTime='10:00', answers=[], expireDate="99", expireTime="11:00", Notify=True, Sequence=1,
                 Name="First")

    """ uuid = models.CharField(max_length=UUID_FIELD)
timestamp = models.DateTimeField
deletedIndicator = models.BooleanField
question = models.ForeignKey(Question, on_delete=models.CASCADE)
user = models.ForeignKey(User, on_delete=models.CASCADE)
Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
Answered = models.BooleanField()"""
    a = Answer(UUID="9872", timestamp=timezone.now(), question=q, user=u, Answer_text="blah", Answered=True)

    def test_modulo(self):
        print("testing Modulo")
        """
        tests if given a date that is not every two weeks it returns false
        """
        time = timezone.now() + datetime.timedelta(days=30)
        non_twoweek = User(identifier="Joel", language="ENG", UUID="12345", timestamp=timezone.now(),
                           deletedIndicator=False, Days_since_start=17, Days_since_last_report=2)
        is_twoweek = User(identifier="Joel", language="ENG", UUID="12345", timestamp=timezone.now(),
                          deletedIndicator=False, Days_since_start=14, Days_since_last_report=2)
        self.assertIs(non_twoweek.time_to_change(), False)
        self.assertIs(is_twoweek.time_to_change(), True)

    def test_save(self):
        print("testing Save")
        """
        tests if item is saved
        :return:s
        """
        self.u.save()
        self.assertTrue(self.u in User.objects.all())
        self.s.save()
        self.q.save()
        self.assertTrue(self.q in Question.objects.all())

    def test_delete(self):
        print("testing delete")
        """
        tests if item is deleted
        :return:
        """
        self.u.save()
        self.u.delete()
        self.assertFalse(self.u in User.objects.all())

    def test_make_question(self):
        print("testing questions")
        for report in debugReport.objects.all():
            try:
                data = report.data
                event = report.data['event']
                if event == "answerQuestion":
                    """
                    set data into variabbles, de dictafy
                    """
                    questionData = data["question"]
                    choices = questionData["choices"]
                    answered_on_day = questionData["answeredOnDay"]
                    askDate = questionData["askDate"]
                    askDay = questionData["askDay"]
                    askDateTime = questionData["askDatetime"]
                    askTime = questionData["askTime"]
                    expireDate = questionData['expireDay']
                    expireTime = questionData['expireTime']
                    sequence = questionData['sequence']
                    name = questionData['name']
                    tag = questionData['tag']
                    text = questionData['text']
                    answer = questionData['answer']
                    createdat = questionData['createdAt']
                    answers = questionData["answers"]
                    responceType = questionData["responseFormat"]
                    print("Workings")
                    if report.kind == "answer":
                        if name == "getDisplayName":
                            """
                            make a new user
                            """
                            u = User(identifier=report.source, language='eng', UUID=report.id,
                                     timestamp=createdat,
                                     deletedIndicator=False, Days_since_start=0,
                                     Days_since_last_report=0)
                            u.save()
                        if name == "activityDebrief":

                            """
                            make a survey

                            """
                            try:
                                survey = Survey.objects.get(questionData["taskId"])
                            except:
                                survey = Survey(UUID=questionData["taskId"], timestamp=askDateTime,
                                                deletedIndicator=False, Name="Activity Debrief")
                            survey.save()
                            try:
                                quest = Question(question_text=text, UUID=report.id, timestamp=createdat,
                                                 deletedIndicator=False,
                                                 responceType=responceType, tag=tag, choices=choices,
                                                 referenceToSurvey=survey,
                                                 reminders=False, askDate=askDay, askTime=askTime,
                                                 preferenceToSet="Nothing",
                                                 answers=answers, expireDate=expireDate, expireTime=expireTime,
                                                 Notify=False,
                                                 Sequence=sequence, Name=name)
                                quest.save()
                            except():
                                print("error is here")

            except(KeyError):
                print("You got a key error")
            self.assertTrue(quest in Question.objects.all())






