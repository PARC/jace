from rest_framework import serializers

from communications.models import *


class ReportSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = FittleReport
        fields = ("studyName", "kind", "source", "data", "shared", "createdAt")