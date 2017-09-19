from django.db.models.signals import post_save
from django.dispatch import receiver

from communications.models import *
from user_model.models import *
import requests

"""
Updates all of the other parts of the database. This activates whenever there is a post made to communications/reports.
"""
# api not implemented yet

# @receiver(post_save, sender=Report)
# def get_missing(sender, **kwargs):
#    r = requests.get('localhost:3000/serviceapi/unreported/woof')
#    report = Report(r)
#    report.save()
