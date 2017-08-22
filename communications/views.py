# Create your views here.
import redis
from rest_framework import generics

from communications.seriealizers import *
from user_model.serializers import *

r = redis.StrictRedis(host='localhost', port=32772, db=0)


class report_list(generics.ListCreateAPIView):
    """
    List all Reports, or create a new Report.
    """
    queryset = FittleReport.objects.all()
    serializer_class = ReportSeriealizer

    def post(self, request, *args, **kwargs):
        return request





class user_list(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class intervention_list(generics.ListCreateAPIView):
    """
    List all Intervention, or create a new Intervention.
    """

    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer


class survey_list(generics.ListCreateAPIView):
    """
    List all Surveys, or create a new Surveys.
    """

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class question_list(generics.ListCreateAPIView):
    """
    List all Surveys, or create a new question.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class answer_list(generics.ListCreateAPIView):
    """
    List all Surveys, or create a new answer.
    """

    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a report.
    """
    queryset = FittleReport.objects.all()
    serializer_class = ReportSeriealizer


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class Intervention_detail(generics.RetrieveUpdateDestroyAPIView):
    """
       Retrieve, update or delete an intervnetion.
       """

    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer


class Survey_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a survey.
    """

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class question_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a question.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class answer_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a answer.
    """

    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer
