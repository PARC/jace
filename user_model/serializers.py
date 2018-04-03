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


from rest_framework import serializers

from user_model.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
