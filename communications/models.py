# Create your models here.
"""
Main API Code
Joel Schooler
"""
from django.contrib.postgres import fields
from django.db import models

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048
SUPER_LONG = 9000
DBZ_LENGTH = 32365


class Report(models.Model):
    """

    Takes all reports from incoming app
    """
    studyName = models.CharField(max_length=MEDIUM_LENGTH)
    kind = models.CharField(max_length=MEDIUM_LENGTH)
    data = fields.JSONField()
    source = models.CharField(max_length=SHORT_LENGTH)
    def __repr__(self):
        return str(self.data)


