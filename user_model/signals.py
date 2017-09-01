from django.db.models.signals import post_save
from django.dispatch import receiver
from communications.models import *
from user_model.models import *
#conn = redis.Redis(port=os.environ['REDIS'].split(':')[1],host=os.environ['REDIS'].split(':')[0])
"""
Updates all of the other parts of the database.
"""


@receiver(post_save, sender=debugReport)
def update_all(sender, **kwargs):
    for report in debugReport.objects.all():
        try:
            data = report.data
            event = report.data['event']
            if report.data["event"] == "answerQuestion":
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
                expireDate = questionData['expireDate']
                expireTime = questionData['expireTime']
                sequence = questionData['sequence']
                name = questionData['name']
                tag = questionData['tag']
                text = questionData['text']
                answer = questionData['answer']
                createdat = questionData['createdAt']
                answers = questionData["answers"]
                name = questionData["name"]
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
                            survey = Survey(UUID=questionData["taskId"],timestamp=askDateTime,deletedIndicator=False,
                        Name="Activity Debrief")

                        """
                        make a question for activity's

                        question_text = models.CharField(max_length=SHORT_LENGTH)
    UUID = models.CharField(max_length=UUID_FIELD, primary_key=True)
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
                        """
                        q = Question(question_text=text,UUID=report.ID,timestamp=createdat,deletedIndicator=False,
                                     responceType=None,tag=tag,choices=choices,referenceToSurvey=survey,reminders=False,
                                     askDate=askDay,askTime=askTime,preferenceToSet=questionData["preferenceToSet"],
                                     answers=answers,expireDate=expireDate,expireTime=expireTime,Notify=False,Sequence=sequence,
                                     Name=name)

        except(KeyError):
            pass


