from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule, created = IntervalSchedule.objects.get_or_create(every=10,
     period=IntervalSchedule.SECONDS)
