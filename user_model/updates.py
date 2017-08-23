from communications.models import *
from user_model.models import *


def update_all():
        for report in debugReport.objects.all():
                data = report.data
                event = report.data['event']
                choices = report.data['choices']
                answered_on_day = report.data["answeredOnDay"]
                askDate = report.data["askDate"]
                askDay = report.data["askDay"]
                askDateTime = report.data["askDatetime"]
                askTime = report.data["askTime"]
                expireDate = report.data['expireDate']
                expireTime = report.data['expireTime']
                sequence = report.data['sequence']
                name = report.data['name']
                tag = report.data['tag']
                text = report.data['text']
                answer = report.data['answer']
                createdat = report.data['createdAt']
                if report.kind == "answer":
                        if name == "getDisplayName":
                                u = User(identifier=report.source, language='eng', UUID=report.id, timestamp=createdat,
                                         deletedindicator=False, startDate=createdat, days_since_start=0,
                                         days_since_last_report=0)
                                u.save()
