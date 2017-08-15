# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from communications.serializers import *


class user_list(APIView):
    """
    List all users, or create a new user.
    """

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class intervention_list(APIView):
    """
    List all Intervention, or create a new Intervention.
    """

    def get(self, request, format=None):
        intervention = Intervention.objects.all()
        serializer = InterventionSerializer(intervention, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class survey_list(APIView):
    """
    List all Surveys, or create a new Surveys.
    """

    def get(self, request, format=None):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class question_list(APIView):
    """
    List all Surveys, or create a new question.
    """

    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class answer_list(APIView):
    """
    List all Surveys, or create a new answer.
    """

    def get(self, request, format=None):
        answer = Answer.objects.all()
        serializer = AnswersSerializer(answer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_detail(APIView):
    """
    Retrieve, update or delete a user.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def Intervention_detail(request, pk):
#     """
#     Retrieve, update or delete an Intervention.
#     """
#     try:
#         intervention = Intervention.objects.get(pk=pk)
#     except Intervention.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = InterventionSerializer(intervention)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = InterventionSerializer(intervention, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         intervention.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def Survey_detail(request, pk):
#     """
#     Retrieve, update or delete a survey.
#     """
#     try:
#         survey = Survey.objects.get(pk=pk)
#     except Survey.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SurveySerializer(survey)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SurveySerializer(Survey, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         survey.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def question_detail(request, pk):
#     """
#     Retrieve, update or delete a survey.
#     """
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = QuestionSerializer(Survey, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def answer_detail(request, pk):
#     """
#     Retrieve, update or delete a survey.
#     """
#     try:
#         answer = Answer.objects.get(pk=pk)
#     except Answer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = AnswersSerializer(answer)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AnswersSerializer(Survey, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
