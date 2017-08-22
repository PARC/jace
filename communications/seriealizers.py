from rest_framework import serializers

from communications.models import *


class ReportSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = FittleReport
        fields = ("userId", "studyName", "kind", "source", "data", "shared", "createdAt")
