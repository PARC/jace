from django.db.models.signals import post_save
from django.dispatch import receiver

from communications.models import *
from user_model.models import *

"""
Updates all of the other parts of the database. This activates whenever there is a post made to communications/reports.
"""


@receiver(post_save, sender=Report)
def update_all(sender, **kwargs):
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
                askDateTime = questionData["askDatetime"]  #timestamp
                askTime = questionData["askTime"]
                expireDate = questionData['expireDay']  #numeric
                expireTime = questionData['expireTime']
                sequence = questionData['sequence']  #numeric
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
                try:
                    u = User.objects.get(studyId=source)
                    Days_since_start = u.Days_since_start
                    Days_since_activity_start = u.Days_since_activity_start
                except:
                    Days_since_start = 0
                    Days_since_activity_start = 0
                if report.kind == "answer":
                    if name == "getDisplayName":
                        """
                        make a new user
                        """
                        u = User(studyId=report.source, language='eng', UUID=report.id,
                                 timestamp=createdat,
                                 deletedIndicator=False, Days_since_start=Days_since_start, Last_day_reported=0,
                                 Days_since_activty_start=Days_since_activity_start)
                        u.save()
                    if name == "activityDebrief":
                        """
                        make a survey
                        """
                        try:
                            survey = Survey.objects.get(questionData["taskId"])
                        except:
                            survey = Survey(UUID=questionData["taskId"], timestamp=askDateTime, deletedIndicator=False,
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
                            answer = Answer(UUID=report.id, timestamp=createdat, deletedIndicator=False, question=quest,
                                            user=user, Answer_text=answer, Answered=bool(answer))
                            answer.save()
                        except():
                            pass

        except(KeyError):
            pass
