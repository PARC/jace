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


class FittleReport(models.Model):
    _id = models.CharField(max_length=UUID_FIELD)
    studyName = models.CharField(max_length=MEDIUM_LENGTH)
    kind = models.CharField(max_length=MEDIUM_LENGTH)
    source = models.CharField(max_length=SHORT_LENGTH, primary_key=True)
    data = fields.JSONField()
    shared = models.CharField(max_length=DBZ_LENGTH)
    createdAt = models.CharField(max_length=SHORT_LENGTH)

    def __repr__(self):
        return str(self._id)
