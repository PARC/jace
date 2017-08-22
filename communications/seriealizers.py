from rest_framework import serializers

from communications.models import *


class ReportSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = FittleReport
        fields = ("_id", "studyName", "kind", "source", "data", "shared", "createdAt")


class DebugReportSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = debugReport
        fields = "data"
