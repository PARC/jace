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


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from communications import views

token = "42istheanswer"
# (?P<token>.*)
urlpatterns = [
    url(r'^reports/$', views.report_list.as_view()),
    url(r'^users/$', views.user_list.as_view()),
    url(r'^surveys/$', views.survey_list.as_view()),
    url(r'^questions/$', views.question_list.as_view()),
    url(r'^answers/$', views.answer_list.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
