from communications.models import *

for report in FittleReport.objects.all():
    if report.kind == "Answer":
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
