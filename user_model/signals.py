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
                            survey = Survey(UUID=questionData["taskId"],timestamp=askDateTime,deletedIndicator=False,Name="Activity Debrief")
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


        except(KeyError):
            pass


