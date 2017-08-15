from rest_framework import serializers

from communications.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'identifier', 'language', 'uuid', 'timestamp', 'deletedIndicator', "startdate", "Days_since_start",
            "Days_since_last_report",)


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ('id', "uuid", "timestamo", "deletedIndicator", "Name", "Intervention_Type", "Setup_Complete", "Is_On",
                  "startdate", "reference_to_user")


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', "uuid", "timestamo", "deletedIndicator", "Name", "Reference_to_Intervention")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text', 'uuid', 'timestamp', 'deletedIndicator', 'responceType', 'responceTypeTime', 'tag',
            'choices',
            "referenceToSurvey", "reminders", "askDate", "askTime", "preferenceToSet", "answers", "expireDate",
            "expireTime",
            "Notify", "Sequence", "Name")


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("uuid", "timestamp", "deletedIndicator", "question", "user", "Answer_text", "Answered")
