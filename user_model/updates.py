from communications.models import *

for report in FittleReport.objects.all():
    report.data
