from rest_framework import serializers

from user_model.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'identifier', 'language', 'UUID', 'timestamp', 'deletedIndicator', "Days_since_start",
            "Days_since_last_report")



class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ("UUID", "timestamp", "deletedIndicator", "Name")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text', 'UUID', 'timestamp', 'deletedIndicator', 'responceType', 'tag',
            'choices',
            "referenceToSurvey", "reminders", "askDate", "askTime", "preferenceToSet", "answers", "expireDate",
            "expireTime",
            "Notify", "Sequence", "Name")


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("uuid", "timestamp", "deletedIndicator", "question", "user", "Answer_text", "Answered")
