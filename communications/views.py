'''
*************************************************************************
*
*  © [2018] PARC Inc., A Xerox Company
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Xerox Corporation.
* The intellectual and technical concepts contained
* herein are proprietary to PARC Inc. and Xerox Corp.,
* and may be covered by U.S. and Foreign Patents,
* patents in process, and may be protected by copyright law.
* This file is subject to the terms and conditions defined in
* file 'LICENSE.md', which is part of this source code package.
*
**************************************************************************
'''


import redis
from rest_framework import generics

from communications.seriealizers import *
from user_model.serializers import *

r = redis.StrictRedis(host='localhost', port=32772, db=0)


class report_list(generics.ListCreateAPIView):
    """
    List all Reports, or create a new Report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSeriealizer


class user_list(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



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
    queryset = Report.objects.all()
    serializer_class = ReportSeriealizer


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer




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
