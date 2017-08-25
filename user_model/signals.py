from django.db.models.signals import post_save
from django.dispatch import receiver

from communications.models import *
from user_model.models import *

"""
Updates all of the other parts of the database.
"""

@receiver(post_save, sender=User)
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
        except(KeyError):
            pass

