# Create your models here.
"""
Main API Code
Joel Schooler
"""
from django.db import models

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048
SUPER_LONG = 9000
DBZ_LENGTH = 32365


class Fittle_Report(models.Model):
    studyname = models.CharField(max_length=MEDIUM_LENGTH),
    kind = models.CharField(max_length=MEDIUM_LENGTH),
    source = models.CharField(max_length=SHORT_LENGTH, primary_key=True),
    data = models.CharField(max_length=DBZ_LENGTH),
    shared = models.BooleanField(),
    createdAt = models.DateTimeField()

    def __repr__(self):
        return str(self.source)
