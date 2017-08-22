from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from communications import views

# (?P<token>.*)
urlpatterns = [
    url(r'^reports/$', views.report_list.as_view()),
    url(r'^users/$', views.user_list.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail.as_view()),
    url(r'^interventions/$', views.intervention_list.as_view()),
    url(r'^interventions/(?P<pk>[0-9]+)/$', views.Intervention_detail.as_view()),
    url(r'^surveys/$', views.survey_list.as_view()),
    url(r'^interventions/(?P<pk>[0-9]+)/$', views.Survey_detail.as_view()),
    url(r'^questions/$', views.question_list.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.question_detail.as_view()),
    url(r'^answers/$', views.answer_list.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.answer_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
