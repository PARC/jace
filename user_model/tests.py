

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone
from communications.models import *
from .models import *

class QuestionModelTests(TestCase):
    u = User(studyId="Joel", language="ENG", UUID="12345", timestamp=timezone.now(), deletedIndicator=False,
             Last_day_reported=0, Days_since_start=0, Days_since_activty_start=0)

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
        non_twoweek = User(studyId="Joel", language="ENG", UUID="12345", timestamp=timezone.now(),
                           deletedIndicator=False, Days_since_start=1, Days_since_activty_start=0)
        is_twoweek = User(studyId="Joel", language="ENG", UUID="12345", timestamp=timezone.now(),
                          deletedIndicator=False,
                          Last_day_reported=0, Days_since_start=0, Days_since_activty_start=0)
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
        r = Report(studyName="KPH", kind="answer", data={
            "event": "answerQuestion",
            "question": {
                "_id": "EwPYgGqnThxQEXqSw",
                "source": "silver@parc.com",
                "tag": "you",
                "name": "getDisplayName",
                "text": "Set the public display name to be seen by your team members.",
                "props": {
                    "minLength": 2,
                    "textLabel": "Display name",
                    "startWithChar": True,
                    "textPlaceholder": "Display name (min 2 chars)"
                },
                "answer": "",
                "askDay": "-1",
                "notify": "false",
                "taskId": "",
                "answers": {},
                "askDate": "2017-09-18T07:00:00.000Z",
                "askTime": "07:00",
                "choices": [],
                "expired": False,
                "answered": False,
                "sequence": 11,
                "username": "silver@parc.com",
                "createdAt": "2017-09-19T18:36:22.829Z",
                "expireDay": "28",
                "expireDate": "2017-10-17T07:00:00.000Z",
                "expireTime": "23:59",
                "askDatetime": "2017-09-18T14:00:00.000Z",
                "noneAllowed": False,
                "answeredOnDay": "",
                "expireDatetime": "2017-10-18T06:59:00.000Z",
                "responseFormat": "text",
                "preferenceToSet": "bio.displayName"
            }, "eventName": "answerQuestion"
        }
                   )
        r.save()
        """
           updates database eachtime a event is posted
           :param sender:
           :param kwargs:
           :return:
           """
        for report in Report.objects.all():  # This runs the update on all items that have been reported
            try:  # makes sure report contains right data type
                data = report.data
                if report.data["event"] == "answerQuestion":
                    """
                    set data into variabbles, read the dictionary, place variables into variables.

                    """
                    questionData = data[
                        "question"]  # this contains a subdictionary of all the data about a question that was asked.
                    choices = questionData["choices"]
                    answered_on_day = questionData["answeredOnDay"]
                    askDate = questionData["askDate"]  # timestamp
                    askDay = questionData["askDay"]  # numeric represenration of day, is iterable
                    askDateTime = questionData["askDatetime"]  # timestamp
                    askTime = questionData["askTime"]
                    expireDate = questionData['expireDay']  # numeric
                    expireTime = questionData['expireTime']
                    sequence = questionData['sequence']  # numeric
                    name = questionData['name']
                    tag = questionData['tag']
                    text = questionData['text']
                    answer = questionData['answer']
                    createdat = questionData['createdAt']
                    answers = questionData["answers"]
                    responceType = questionData["responseFormat"]
                    source = report.source
                    """
                    """
                    if report.kind == "answer":
                        if name == "getDisplayName":
                            """
                            make a new user
                            """
                            u = User(studyId=report.source, language='eng', UUID=report.id,
                                     timestamp=createdat,
                                     deletedIndicator=False, Last_day_reported=0, Days_since_start=0,
                                     Days_since_activty_start=0)
                            u.save()
                        if name == "activityDebrief":
                            """
                            make a survey
                            """
                            try:
                                survey = Survey.objects.get(questionData["taskId"])
                            except:
                                survey = Survey(UUID=questionData["taskId"], timestamp=askDateTime,
                                                deletedIndicator=False,
                                                Name="Activity Debrief")
                            survey.save()
                            """
                            make a question
                            """
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

                            try:
                                """UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
        timestamp = models.DateTimeField()
        deletedIndicator = models.BooleanField()
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        Answer_text = models.CharField(max_length=MEDIUM_LENGTH)
        Answered = models.BooleanField()"""
                                user = User.objects.get(studyId=source)
                                user.Last_day_reported = askDay
                                user.save()
                                self.assertTrue(user in User.objects.all())
                                answer = Answer(UUID=report.id, timestamp=createdat, deletedIndicator=False,
                                                question=quest,
                                                user=user, Answer_text=answer, Answered=bool(answer))
                                answer.save()
                            except():
                                pass

            except(KeyError):
                pass
