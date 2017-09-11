from rest_framework import serializers

from communications.models import *





class ReportSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
